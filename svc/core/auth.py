from __future__ import annotations

from datetime import datetime, timedelta, timezone
from functools import lru_cache
from typing import Annotated, Any

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

from svc.core.config import Settings, get_settings


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    disabled: bool = False


class UserInDB(User):
    hashed_password: str


type UserRecord = dict[str, str]


pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
router = APIRouter()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


@lru_cache
def get_fake_users_db(username: str, password: str) -> dict[str, UserRecord]:
    return {
        username: {
            "username": username,
            "hashed_password": get_password_hash(password),
        }
    }


def get_user(db: dict[str, UserRecord], username: str | None) -> UserInDB | None:
    if username not in db:
        return None
    user_dict = db[username]
    return UserInDB(**user_dict)


def authenticate_user(
    fake_db: dict[str, UserRecord],
    username: str,
    password: str,
) -> UserInDB | None:
    user = get_user(fake_db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(
    data: dict[str, Any],
    secret_key: str,
    algorithm: str,
    expires_delta: timedelta | None = None,
) -> str:
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(tz=timezone.utc) + expires_delta
    else:
        expire = datetime.now(tz=timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        secret_key,
        algorithm=algorithm,
    )
    return encoded_jwt


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.api_secret_key,
            algorithms=[settings.api_algorithm],
        )
        username = payload.get("sub")

        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)

    except InvalidTokenError:
        raise credentials_exception

    user = get_user(
        get_fake_users_db(settings.api_username, settings.api_password),
        username=token_data.username,
    )

    if user is None:
        raise credentials_exception
    return user


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    settings: Annotated[Settings, Depends(get_settings)],
) -> dict[str, str]:
    user = authenticate_user(
        get_fake_users_db(settings.api_username, settings.api_password),
        form_data.username,
        form_data.password,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=settings.api_access_token_expire_minutes,
    )
    access_token = create_access_token(
        data={"sub": user.username},
        secret_key=settings.api_secret_key,
        algorithm=settings.api_algorithm,
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}

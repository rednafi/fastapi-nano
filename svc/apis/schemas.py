from pydantic import BaseModel


class RandomNumbers(BaseModel):
    seed: int
    random_first: int
    random_second: int

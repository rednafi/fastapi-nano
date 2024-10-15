<div align="center">

![logo](https://user-images.githubusercontent.com/30027932/134270064-baecfbec-b3e7-4cb7-a07e-c11a58526260.png)

[![Mentioned in Awesome <INSERT LIST NAME>](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/mjhea0/awesome-fastapi#boilerplate)
[![License](https://img.shields.io/cocoapods/l/AFNetworking?style=flat-square)](https://github.com/rednafi/think-asyncio/blob/master/LICENSE)
[![Twitter](https://img.shields.io/twitter/follow/rednafi?style=flat-square)](https://twitter.com/rednafi)

</div>

## Description

This is a simple [FastAPI][fastapi] template that follows Flask's [blueprint][blueprint]
directory structure.

## Features

-   Uses [FastAPI][fastapi] to build the HTTP API endpoints.

-   Served via [Gunicorn](gunicorn) with multiple [Uvicorn][uvicorn] workers. Uvicorn is a
    lightning-fast "ASGI" server. It runs asynchronous Python web code in a single process.

-   Simple reverse-proxying with [Caddy][caddy].

-   OAuth2 (with hashed password and Bearer with JWT) based authentication.

-   [CORS (Cross Origin Resource Sharing)][cors] enabled.

-   Flask inspired divisional directory structure, suitable for small to medium backend
    development.

-   Uses [uv][uv] for dependency management, enabling shorter build time.

-   Dockerized using **python:3.13-slim** image and optimized for size. Dockerfile for
    Python 3.12 and 3.11 can also be found in the `dockerfiles` directory.

## Quickstart

### Run in containers

-   Clone the repo and navigate to the root folder.

-   To run the app using Docker, make sure you've got [Docker][docker] installed on your
    system. From the project's root directory, run:

    ```sh
    make run-container
    ```

### Or, run locally

If you want to run the app locally, without using Docker, then:

-   Clone the repo and navigate to the root folder.

-   Install [uv][uv] for dependency management.

-   Create a virtual environment:

    ```sh
    uv venv -p 3.13
    ```

-   Activate the environment. Run:

    ```sh
    source .venv/bin/activate
    ```

-   Install the dependencies. Run:

    ```sh
    uv sync --frozen
    ```

-   Start the app. Run:

    ```sh
    make run-local
    ```

### Explore the endpoints

-   To play around with the APIs, go to the following link on your browser:

    ```sh
    http://localhost:5002/docs
    ```

    This will take you to an UI like below:

    ![Screenshot from 2020-06-21 22-15-18][screenshot_1]

-   Press the `authorize` button on the right and add _username_ and _password_. The APIs
    use OAuth2 (with hashed password and Bearer with JWT) based authentication. In this
    case, the username and password is `ubuntu` and `debian` respectively.

    ![Screenshot from 2020-06-21 22-18-25][screenshot_2]

    Clicking the `authorize` button will bring up a screen like this:

    ![Screenshot from 2020-06-21 22-18-59][screenshot_3]

-   Then select any of the `api_a` or `api_b` APIs and put an integer in the number box and
    click the `authorize` button.

    ![Screenshot from 2020-06-21 22-31-19][screenshot_4]

-   Hitting the API should give a json response with random integers.

    ![Screenshot from 2020-06-21 22-32-28][screenshot_5]

-   Also, notice the `curl` section in the above screen shot. You can directly use the
    highlighted curl command in your terminal. Make sure you've got `jq` installed in your
    system.

    ```sh
    curl -X GET "http://localhost:5002/api_a/22" \
            -H "accept: application/json" \
            -H "Authorization: Bearer $(curl -X POST "http://localhost:5002/token" \
                            -H "accept: application/x-www-form-urlencoded" \
                            -d "username=ubuntu&password=debian" | jq -r ".access_token")"
    ```

    This should show a response like this:

    ```json
    {
        "seed": 22,
        "random_first": 5,
        "random_second": 13
    }
    ```

### Testing, Linting, and Maintenance

-   Run tests with `make tests` (uses [pytest][pytest]).
-   Lint with [ruff] and check types with [mypy] using `make lint`.
-   Update dependencies with `make dep-update`.
-   Stop containers with `make kill-container`.

## Directory structure

This shows the folder structure of the default template.

```txt
fastapi-nano
├── svc                           # primary service folder
│   ├── apis                      # this houses all the API packages
│   │   ├── api_a                 # api_a package
│   │   │   ├── __init__.py       # empty init file to make the api_a folder a package
│   │   │   ├── mainmod.py        # main module of api_a package
│   │   │   └── submod.py         # submodule of api_a package
│   │   └── api_b                 # api_b package
│   │       ├── __init__.py       # empty init file to make the api_b folder a package
│   │       ├── mainmod.py        # main module of api_b package
│   │       └── submod.py         # submodule of api_b package
│   ├── core                      # this is where the configs live
│   │   ├── auth.py               # authentication with OAuth2
│   │   ├── config.py             # sample config file
│   │   └── __init__.py           # empty init file to make the config folder a package
│   ├── __init__.py               # empty init file to make the app folder a package
│   ├── main.py                   # main file where the fastAPI() class is called
│   ├── routes                    # this is where all the routes live
│   │   └── views.py              # file containing the endpoints for api_a and api_b
│   └── tests                     # test package
│       ├── __init__.py           # empty init file to make the tests folder a package
│       ├── test_api.py           # integration testing the API responses
│       └── test_functions.py     # unit testing the underlying functions
├── dockerfiles                   # directory containing all the dockerfiles
├── .env                          # env file containing app variables
├── Caddyfile                     # simple reverse-proxy with caddy
├── docker-compose.yml            # docker-compose file
├── pyproject.toml                # pep-518 compliant config file
└── uv.lock                       # pinned app and dev dependencies
```

In the above structure, `api_a` and `api_b` are the main packages where the code of the APIs
live and they are exposed by the endpoints defined in the `routes` folder. Here, `api_a` and
`api_b` have identical logic. These are dummy APIs that take an integer as input and return
two random integers between zero and the input value. The purpose of including two identical
APIs in the template is to demonstrate how you can decouple the logics of multiple APIs and
then assemble their endpoints in the routes directory. The following snippets show the logic
behind the dummy APIs.

This is a dummy submodule that houses a function called `random_gen` which generates a
dictionary of random integers.

```python
# This a dummy module
# This gets called in the module_main.py file
from __future__ import annotations
import random


def rand_gen(num: int) -> dict[str, int]:
    num = int(num)
    d = {
        "seed": num,
        "random_first": random.randint(0, num),
        "random_second": random.randint(0, num),
    }
    return d
```

The `main_func` in the primary module calls the `rand_gen` function from the submodule.

```python
from __future__ import annotations
from svc.api_a.submod import rand_gen


def main_func(num: int) -> dict[str, int]:
    d = rand_gen(num)
    return d
```

The endpoint is exposed like this:

```python
# svc/routes/views.py
from __future__ import annotations
#... codes regarding authentication ...

# endpoint for api_a (api_b looks identical)
@router.get("/api_a/{num}", tags=["api_a"])
async def view_a(num: int, auth: Depends =Depends(get_current_user)) -> dict[str, int]:
    return main_func_a(num)
```

So hitting the API with a random integer will give you a response like the following:

```json
{
  "seed": 22,
  "random_first": 27,
  "random_second": 20
}
```

## Further modifications

-   You can put your own API logic following the shape of `api_a` and `api_b` packages.
    You'll have to add additional directories like `api_a` or `api_b` if you need to expose
    more endponts.

-   Then expose the API URLs in the `routes/views.py` file. You may choose to create
    multiple `views` files to organize your endpoint URLs.

-   This template uses OAuth2 based authentication and it's easy to change that. FastAPI
    docs has a comprehensive list of the available [authentication][fastapi_security]
    options and instructions on how to use them.

-   During prod deployment, you might need to fiddle with the reverse-proxy rules in the
    Caddyfile.

## Resources

-   [Flask divisional folder structure][blueprint]
-   [Deploying APIs built with FastAPI](https://fastapi.tiangolo.com/deployment/)
-   [Reverse proxying with Caddy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy)

[blueprint]: https://flask.palletsprojects.com/en/2.3.x/blueprints/
[caddy]: https://caddyserver.com/docs/
[cors]: https://fastapi.tiangolo.com/tutorial/cors/
[docker]: https://www.docker.com/
[fastapi]: https://fastapi.tiangolo.com/
[fastapi_security]: https://fastapi.tiangolo.com/tutorial/security/
[gunicorn]: https://gunicorn.org/
[httpx]: https://www.python-httpx.org/
[pytest]: https://docs.pytest.org/en/stable/
[ruff]: https://astral.sh/ruff
[uvicorn]: https://uvicorn.org/
[uv]: https://docs.astral.sh/uv/
[screenshot_1]:
    https://user-images.githubusercontent.com/30027932/85229723-5b721880-b40d-11ea-8f03-de36c07a3ce5.png
[screenshot_2]:
    https://user-images.githubusercontent.com/30027932/85229725-5e6d0900-b40d-11ea-9c37-bbee546f84a8.png
[screenshot_3]:
    https://user-images.githubusercontent.com/30027932/85229729-6036cc80-b40d-11ea-877e-7421b927a849.png
[screenshot_4]:
    https://user-images.githubusercontent.com/30027932/85229992-fcad9e80-b40e-11ea-850d-9ca86259d463.png
[screenshot_5]:
    https://user-images.githubusercontent.com/30027932/85230016-25359880-b40f-11ea-9196-c46fd72a760c.png

<div align="center">
✨ 🍰 ✨
</div>

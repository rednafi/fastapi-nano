<div align="center">

# FastAPI Nano

🐍 A minimalistic FastAPI template with factory pattern architecture

</div>

## Description

This [FastAPI](https://fastapi.tiangolo.com/) template incorporates factory pattern architecture with [divisional folder structure](https://exploreflask.com/en/latest/blueprints.html#divisional) for API oriented micro-service development. The architecture is similar to what you'd get with Flask's [Blueprint](https://exploreflask.com/en/latest/blueprints.html).

## Features

* It uses [FastAPI]() framework for API development. FastAPI is a modern, highly performant, web framework for building APIs with Python 3.6+.

* The APIs are served with [Uvicorn]() server. Uvicorn is a lightning-fast "ASGI" server. It runs asynchronous Python web code in a single process.

* [Gunicorn]() is used here to manage Uvicorn and run multiple of these concurrent processes. That way, you get the best of concurrency and parallelism.

* Password based http basic authentication to secure the endpoints.

* [CORS (Cross Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/) enabled.

* Flask inspired divisional folder structure better decoupling and encapsulation. This is suitable for small to medium backend development.

* Dockerized using [uvicorn-gunicorn-fastapi-docker]( https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
). This image will set a sensible configuration based on the server it is running on (the amount of CPU cores available) without making sacrifices.

    It has sensible defaults, but you can configure it with environment variables or override the configuration files.

## Folder Structure

```
.
├── app                       # primary application folder
│   ├── api_a                 # api_a package
│   │   ├── __init__.py       # empty init file to make the api_a folder a package
│   │   ├── mainmod.py        # main module of api_a package
│   │   └── submod.py         # submodule of api_a package
│   ├── api_b                 # api_b package
│   │   ├── __init__.py       # empty init file to make the api_b folder a package
│   │   ├── mainmod.py        # main module of api_b package
│   │   └── submod.py         # submodule of api_b package
│   ├── core                  # this is where the configs live
│   │   ├── config.py         # sample config file
│   │   └── __init__.py       # empty init file to make the config folder a package
│   ├── __init__.py           # empty init file to make the app folder a package
│   ├── main.py               # main file where the fastAPI() class is called
│   ├── routes                # this is where all the routes live
│   │   └── views.py          # file containing the endpoints of api_a and api_b
│   └── tests                 # test package
│       ├── __init__.py       # empty init file to make the tests folder a package
│       └── test_api.py       # test files
├── .dockerignore             # list of files and folders for docker to ignore
├── .env                      # sample .env file to pull configs from
├── .gitignore                # list of files and folders for VCS to ignore
├── .isort.cfg                # isort config file
├── .pre-commit-config.yaml   # pre-commit config file
├── docker-compose.yml        # docker-compose file
├── Dockerfile                # dockerfile
├── poetry.lock               # lock file for dependencies
├── pyproject.toml            # human readable dependency list
└── README.md                 # meta
```

In the above structure, `api_a` and `api_b` are the main packages where the code of the APIs live and they are exposed by the endpoints defined in the `routes` folder. Here, `api_a` and `api_b` are dummy APIs that take an integer and return two random integers between zero and the input value.

The following snippets show the logic behind the dummy APIs (`api_b` looks identical to `api_a`):

```python
# app/api_a/submod.py

# This a dummy module
# This gets called in the module_main.py file

import random


def random_dict(num: int) -> dict:
    num = int(num)
    d = {
        "seed": num,
        "random_first": random.randint(0, num),
        "random_second": random.randint(0, num),
    }
    return d

```

```python
# app/api_a/mainmod.py

from app.api_a.submod import random_dict


def func_main(num: int) -> dict:
    d = random_dict(num)
    return d
```

So hitting the API with a random integer will give you a response like the following:

```json
{
  "seed": 34,
  "random_first": 27,
  "random_second": 20
}
```


## Quickstart

* Clone the repository.
    ```
    git clone git@github.com:rednafi/fastapi-nano.git
    ```

* Go to the root folder and run:
    ```
    docker-compose up -d
    ```



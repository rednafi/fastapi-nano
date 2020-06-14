<div align="center">

![logo](https://user-images.githubusercontent.com/30027932/83198400-ec343c00-a160-11ea-8bec-28f0d09b16de.png)

</div>

## Description

This is a minimalistic and extensible [FastAPI](https://fastapi.tiangolo.com/) template that incorporates factory pattern architecture with [divisional folder structure](https://exploreflask.com/en/latest/blueprints.html#divisional). It's suitable for developing small to medium sized API oriented micro-services. The architecture is similar to what you'd get with Flask's [Blueprint](https://exploreflask.com/en/latest/blueprints.html).

## Features

* It uses [FastAPI](https://fastapi.tiangolo.com/) framework for API development. FastAPI is a modern, highly performant, web framework for building APIs with Python 3.6+.

* The APIs are served with [Uvicorn](https://www.uvicorn.org/) server. Uvicorn is a lightning-fast "ASGI" server. It runs asynchronous Python web code in a single process.

* [Gunicorn](https://gunicorn.org/) is used here to manage Uvicorn and run multiple of these concurrent processes. That way, you get the best of concurrency and parallelism.

* Password based http basic authentication to secure the endpoints.

* [CORS (Cross Origin Resource Sharing)](https://fastapi.tiangolo.com/tutorial/cors/) enabled.

* Flask inspired divisional folder structure better decoupling and encapsulation. This is suitable for small to medium backend development.

* Dockerized using [uvicorn-gunicorn-fastapi-docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker). This image will set a sensible configuration based on the server it is running on (the amount of CPU cores available) without making sacrifices.

    It has sensible defaults, but you can configure it with environment variables or override the configuration files.

## Quickstart

### Spin Up the Cookiecutter
* Install cookiecutter

* Go to your project folder and run

```bash
cookiecutter https://github.com/rednafi/fastapi-nano.git --checkout dev
```

* Follow the prompts to generate your project
    ```

    ```

### Run the Containers

* Go to your template folder and run:

    ```bash
    docker-compose up -d
    ```

### Check the APIs

* To play around with the APIs, go to the following link on your browser:

    ```
    http://localhost:5000/docs
    ```

    This will take you to an UI like below:

    ![Screenshot from 2020-05-29 02-22-36](https://user-images.githubusercontent.com/30027932/83190668-95c10080-a154-11ea-873b-d8fe80d9c132.png)

* Press the `authorize` button on the right and add username and password. The APIs use basic password based authentication. In this case, the username and password is `rednafi` and `ubuntu` respectively.

* Then select any of the APIs and put an integer in the number box and click the `execute` button.

    ![Screenshot from 2020-05-29 02-35-43](https://user-images.githubusercontent.com/30027932/83191125-5810a780-a155-11ea-8cc7-8c4f4694fbc5.png)

* Hitting the API should give a json response with random integers.

    ![Screenshot from 2020-05-29 02-42-34](https://user-images.githubusercontent.com/30027932/83191591-1a604e80-a156-11ea-930f-4a805d1f631c.png)

* Also, notice the `curl` section in the above screen shot. You can directly use the highlighted curl command in your terminal.

    ```bash
    curl -X GET "http://localhost:5000/api-a/34" -H "accept: application/json" -H "Authorization: Basic cmVkbmFmaTp1YnVudHU="
    ```

    This should show a response like this:

    ```json
    {"seed":34,"random_first":13,"random_second":27}
    ```

* To test the `GET` APIs with Python, you can use a http client library like [httpx](https://www.python-httpx.org/):

    ```python
    import httpx

    headers = {
        "accept": "application/json",
        "Authorization": "Basic cmVkbmFmaTp1YnVudHU=",
    }

    with httpx.Client() as client:
        response = client.get("http://localhost:5000/api-a/34", headers=headers)
        print(response.json())
    ```


## Folder Structure

This shows the folder structure of the default template.

```
fastapi-nano
├── app                             # primary application folder
│   ├── apis                        # this houses all the API packages
│   │   ├── api_a                   # api_a package
│   │   │   ├── __init__.py         # empty init file to make the api_a folder a package
│   │   │   ├── mainmod.py          # main module of api_a package
│   │   │   └── submod.py           # submodule of api_a package
│   │   └── api_b                   # api_b package
│   │       ├── __init__.py         # empty init file to make the api_b folder a package
│   │       ├── mainmod.py          # main module of api_b package
│   │       └── submod.py           # submodule of api_b package
│   ├── core                        # this is where the configs live
│   │   ├── config.py               # sample config file
│   │   └── __init__.py             # empty init file to make the config folder a package
│   ├── __init__.py                 # empty init file to make the app folder a package
│   ├── main.py                     # main file where the fastAPI() class is called
│   ├── routes                      # this is where all the routes live
│   │   └── views.py                # file containing the endpoints of api_a and api_b
│   └── tests                       # test package
│       ├── __init__.py             # empty init file to make the tests folder a package
│       └── test_api.py             # test files
├── docker-compose.yml              # docker-compose file
├── Dockerfile                      # dockerfile
├── LICENSE                         # MIT license
├── mypy.ini                        # type checking configs
├── poetry.lock                     # lock file for dependencies
└── pyproject.toml                  # human readable dependency list
```

In the above structure, `api_a` and `api_b` are the main packages where the code of the APIs live and they are exposed by the endpoints defined in the `routes` folder. Here, `api_a` and `api_b` have identical logic. Basically these are dummy APIs that take an integer as input and return two random integers between zero and the input value. The purpose of including two identical APIs in the template is to demonstrate how you can decouple the logics of muliple APIs and then assemble their endpoints in the routes directory. The following snippets show the logic behind the dummy APIs.

This is a dummy submodule that houses a function called `random_gen` which basically generates a dict of random integers.

```python
# This a dummy module
# This gets called in the module_main.py file

import random
from typing import Dict


def rand_gen(num: int) -> Dict[str, int]:
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
from typing import Dict

from app.api_a.submod import rand_gen


def main_func(num: int) -> Dict[str, int]:
    d = rand_gen(num)
    return d
```

The endpoint is exposed like this:

```python
# app/routes/views.py

#... codes regarding authentication ...

# endpoint for api_a (api_b looks identical)
@router.get("/api_a/{num}", tags=["api_a"])
async def views(num: int, auth=Depends(authorize)) -> Dict[str, int]:
    if auth is True:
        return main_func_a(num)
```

So hitting the API with a random integer will give you a response like the following:

```json
{
  "seed": 34,
  "random_first": 27,
  "random_second": 20
}
```

## Further Modifications

* You can put your own API logics in the shape of `api_a` and `api_b` packages. You'll have to add additional directories like `api_a` and `api_b` if you need more APIs.

* Then expose the APIs in the `routes/views.py` file. You may choose to create multiple `views` files to organize your endpoints.

* This template uses basic password based authentication and it's easy to change that. FastAPI docs has a comprehensive list of the available [authentication options](https://fastapi.tiangolo.com/tutorial/security/) and instructions on how to use them.

* During deployment, you may need to change the host name and port number. To do so, just change the values of `HOST` and `PORT` variables under the `environment` section in the `docker-compose.yml` file.

* Here, containerization has been done using FastAPI author's `python3.8-slim` based [uvicorn-gunicorn-fastapi-docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) image. You may want to use a different base image that caters your usage. A few viable options are listed [here](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker#tiangolouvicorn-gunicorn-fastapi).

* Although this template uses [sensible](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker#tiangolouvicorn-gunicorn-fastapi) `Uvicorn-Gunicorn` defaults, it exposes a few configs under the `environment` section in the `docker-compose.yml` file. Should you choose to tinker with them, you can do it there. Also, you can use a custom `Gunicorn` config file and point the location of the `custom_gunicorn_conf.py` file in the `GUNICORN_CONF` variable.


## Stack

* [FastAPI](https://fastapi.tiangolo.com/)
* [Httpx](https://www.python-httpx.org/)
* [Uvicorn](https://www.uvicorn.org/)
* [Gunicorn](https://gunicorn.org/)
* [Poetry](https://python-poetry.org/)
* [Pydantic](https://pydantic-docs.helpmanual.io/)
* [Starlette](https://www.starlette.io/)
* [Docker](https://www.docker.com/)
* [Pytest](https://docs.pytest.org/en/latest/)

## Resources

* [Docker image: uvicorn-gunicorn-fastapi-docker](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)
* [Flask divisional folder structure](https://exploreflask.com/en/latest/blueprints.html#divisional)
* [Deploying APIs built with FastAPI](https://fastapi.tiangolo.com/deployment/)


<div align="center">

*[=== rednafi ===](https://twitter.com/rednafi)*

</div>

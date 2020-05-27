# fastapi-nano
Minimal fastAPI template with https and basic authentication

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
│   ├── main.py               # main file where fastAPI() class is called
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
├── README.md                 # meta
└── requirements.txt          # requirements file
```

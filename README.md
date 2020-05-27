# fastapi-nano
Minimal fastAPI template with https and basic authentication

```
.
├── app                    # primary application folder
│   ├── api_a              # api_a package
│   │   ├── __init__.py    # empty init file to make the api_a folder a package
│   │   ├── mainmod.py     # main module of api_a package
│   │   └── submod.py      # submodule of api_a package
│   ├── api_b              # api_b package
│   │   ├── __init__.py    # empty init file to make the api_b folder a package
│   │   ├── mainmod.py     # main module of api_b package
│   │   └── submod.py      # submodule of api_b package
│   ├── core               # this is where the configs live
│   │   ├── config.py      # sample config file
│   │   └── __init__.py    # empty init file to make the config folder a package
│   ├── __init__.py        # empty init file to make the app folder a package
│   ├── main.py            # main file where fastAPI() class is called
│   ├── routes             # this is where all the routes live
│   │   └── views.py       # file containing the endpoints of api_a and api_b
│   └── tests              # test package
│       ├── __init__.py    # empty init file to make the tests folder a package
│       └── test_api.py    # test files
├── docker-compose.yml     # docker-compose file
├── Dockerfile             # dockerfile
├── README.md              # meta
├── .env                   # example .env file for configs
└── requirements.txt       # requirements file
```

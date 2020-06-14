from typing import Dict

from app.apis.{{cookiecutter.api1}}.submod import rand_gen


def main_func(num: int) -> Dict[str, int]:
    d = rand_gen(num)
    return d

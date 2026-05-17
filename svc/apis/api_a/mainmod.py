from svc.apis.schemas import RandomNumbers

from .submod import rand_gen


def main_func(num: int) -> RandomNumbers:
    return rand_gen(num)

from typing import Dict

from .submod import rand_gen


def main_func(num: int) -> Dict[str, int]:
    d = rand_gen(num)
    return d

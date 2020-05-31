from typing import Dict

from app.api_a.submod import rand_gen


def main_func(num: int) -> Dict[str, int]:
    d = rand_gen(num)
    return d

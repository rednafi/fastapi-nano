# This is a dummy module.
# This gets called in mainmod.py.

import random

from svc.apis.schemas import RandomNumbers


def rand_gen(num: int) -> RandomNumbers:
    num = int(num)
    return RandomNumbers(
        seed=num,
        random_first=random.randint(0, num),
        random_second=random.randint(0, num),
    )

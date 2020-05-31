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

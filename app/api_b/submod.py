# This a dummy module
# This gets called in the module_main.py file

import random


def rand_gen(num: int) -> dict:
    num = int(num)
    d = {
        "seed": num,
        "random_first": random.randint(0, num),
        "random_second": random.randint(0, num),
    }
    return d

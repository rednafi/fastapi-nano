# This a dummy module
# This gets called in the module_main.py file

import random


def random_dict(num: int):
    num = int(num)
    d = {
        "seed": num,
        "random_first": random.randint(0, num),
        "random_second": random.randint(0, num),
    }
    return d

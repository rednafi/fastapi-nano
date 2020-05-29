from app.api_a.submod import rand_gen


def main_func(num: int) -> dict:
    d = rand_gen(num)
    return d

from app.api_b.submod import rand_gen


def main_func(num: int) -> dict:
    d = rand_gen(num)
    return d

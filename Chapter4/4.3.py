import time
from functools import wraps


def decoration(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        spend = time.time() - start
        print(f"花费时间为{spend}")

    return inner


@decoration
def frange(start, stop, increament):
    x = start
    while x < stop:
        yield x
        x += increament


if __name__ == '__main__':
    frange(1, 10, 1)
    range(1, 10, 2)
    jrange = decoration(range)
    jrange(1, 10, 1)
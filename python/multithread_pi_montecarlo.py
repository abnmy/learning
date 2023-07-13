# TODO perfect example to test multi thread

from math import sqrt, pi as python_pi
from random import random as rand0_1f


def is_in_circle(x: float, y: float, r=1.0) -> bool:
    return sqrt(x**2 + y**2) <= r


def montecarlo_pi(n: int) -> float:
    quarter_pi = sum(is_in_circle(rand0_1f(), rand0_1f()) for _ in range(n))
    return quarter_pi / (n>>2)  # quarter_pi * 4 / n



if __name__ == "__main__":
    print(python_pi)
    print(montecarlo_pi(10_000_000))

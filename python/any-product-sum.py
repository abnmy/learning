"""
Test if a given value can be obtained by adding a number from each list.

The first function is the fastest.
Code is compatible with python 2 and python 3.
"""
from itertools import product


def fastest(list_a, list_b, value):
    return any(a + b == value for a in list_a for b in list_b)


def t2(list_a, list_b, value):
    return any(a + b == value for a, b in product(list_a, list_b))


def t3(list_a, list_b, value):
    return any(s == value for s in map(sum, product(list_a, list_b)))


if __name__ == "__main__":
    import timeit
    NUMBER = 1000000

    FUNCTIONS = (
        "fastest",
        "t2",
        "t3",
    )

    # Run
    times = []
    for function in FUNCTIONS:
        stmt = "%s([1,2,3,4],[10,20,30,40],42)" % function
        setup = "from __main__ import %s" % function
        time = timeit.timeit(stmt, setup, number=NUMBER)

        times.append(time)

    # Display results
    for function, time in zip(FUNCTIONS, times):
        result = "time %s: %.3f" % (function, time)

        print(result)

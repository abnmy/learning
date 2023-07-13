"""
Test if a given value can be obtained by adding a number from each list.
// Code is compatible with python 2 and python 3.
"""
from itertools import product


def f1(list_a, list_b, value):
    return any(a + b == value for a in list_a for b in list_b)


def f2(list_a, list_b, value):
    return any(a + b == value for a, b in product(list_a, list_b))


def f3(list_a, list_b, value):
    return any(s == value for s in map(sum, product(list_a, list_b)))


if __name__ == "__main__":
    import timeit
    ITERATION = 1000000

    FUNCTIONS = (
        "f1",
        "f2",
        "f3",
    )

    # Run
    results = []
    for function in FUNCTIONS:
        stmt = "%s([1,2,3,4],[10,20,30,40],42)" % function
        setup = "from __main__ import %s" % function
        time = timeit.timeit(stmt, setup, number=ITERATION)

        results.append((function, time))

    # Display
    for function, time in sorted(results, key=lambda n:n[1], reverse=False):
        print("time %s: %.3f" % (function, time))

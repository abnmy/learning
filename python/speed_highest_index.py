"""
Find the index of the highest value.

The first function is the fastest.
Code is compatible with python 2 and python 3.
"""
from operator import itemgetter

HEIGHTS = tuple(range(1000))  # HEIGHTS = (0, 1, 2, ..., 998, 999)


def fastest():
    index = HEIGHTS.index(max(HEIGHTS))

    assert index == 999


def f2():
    index, top = 0, 0

    for i, height in enumerate(HEIGHTS):
        if top < height:
            index, top = i, height

    assert index == 999


def f3():
    index, _ = max(enumerate(HEIGHTS), key=itemgetter(1))

    assert index == 999


def f3_bis():  # lambda is slower than itemgetter
    index, _ = max(enumerate(HEIGHTS), key=lambda h: h[1])

    assert index == 999


def f4():
    index, top = 0, 0

    i = 0
    while i < len(HEIGHTS):
        if top < HEIGHTS[i]:
            index, top = i, HEIGHTS[i]
        i += 1

    assert index == 999


if __name__ == '__main__':
    import timeit
    NUMBER = 2000

    FUNCTIONS = (
        "fastest",
        "f2",
        "f3",
        "f3_bis",
        "f4"
    )

    # Run
    times = []
    for function in FUNCTIONS:
        stmt = "%s()" % function
        setup = "from __main__ import %s" % function
        time = timeit.timeit(stmt, setup, number=NUMBER)
        times.append(time)

    # Display results
    for function, time in zip(FUNCTIONS, times):
        result = "time %s: %.3f" % (function, time)
        print(result)

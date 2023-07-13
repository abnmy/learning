"""
Find the index of the highest value.

The first function is the fastest.
"""
from operator import itemgetter


ITERATION = 2000
STMT_TMPL = "$f()"

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

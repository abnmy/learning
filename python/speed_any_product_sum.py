"""
Test if a given value can be obtained by adding a number from each list.
"""
from itertools import product

ITERATION = 100000
SETUP_TMPL = f"from {__name__} import $f"
STMT_TMPL = "$f([1,2,3,4],[10,20,30,40],42)"


def f1(list_a, list_b, value):
    return any(a + b == value for a in list_a for b in list_b)


def f2(list_a, list_b, value):
    return any(a + b == value for a, b in product(list_a, list_b))


def f3(list_a, list_b, value):
    return any(s == value for s in map(sum, product(list_a, list_b)))

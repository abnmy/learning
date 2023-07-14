from itertools import chain


SUDOKU_GRID_SAMPLE="""
1 9 8 7 6 5 4 3 2
7 6 5 4 3 2 1 8 9
4 3 2 1 9 8 6 5 7
9 8 1 5 4 6 2 7 3
2 7 6 9 1 3 8 4 5
5 4 3 8 2 7 9 1 6
6 1 7 3 8 9 5 2 4
3 2 4 6 5 1 7 9 8
8 5 9 2 7 4 3 6 1
"""

# A valid sudoku set must contains nine elements from 1 to 9
VALID_SUDOKU_SET = frozenset(range(1,10))


def is__valid_sudoku_set(sudoku_set) -> bool:
    return set(sudoku_set) == VALID_SUDOKU_SET  


def group_by3(iterable, n=3):
    return zip(* [iter(iterable)] * n)  # iterable[:3], iterable[3:6], iterable[6:]


def is__complete(grid) -> bool:
    # Define rows, columns and squares to check the 27 combinations

    rows = grid

    # zip fetches one element of each row a.k.a. column by column
    columns = zip(*grid)

    # first loop: fetches the rows 3 by 3
    # second loop: the first three elements of the three rows a.k.a. the square
    squares = (
        sq0 + sq1 + sq2  # flatten ((1, 9, 8), (7, 6, 5), (4, 3, 2))
        for three_rows in group_by3(rows)
        for sq0, sq1, sq2 in zip(*map(group_by3, three_rows))
    )

    return all(map(is__valid_sudoku_set, chain(rows, columns, squares)))


if __name__ = "__main__":
    # Convert nine rows in sudoku grid
    # sudoku_grid = (map(int, input().split()) for _ in range(9))

    sudoku_grid = (map(int, row.split()) for row in SUDOKU_GRID_SAMPLE.strip().split('\n'))

    print(is__complete(sudoku_grid))

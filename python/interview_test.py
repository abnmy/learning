"""
M
O
B
E
Y
E
"""
import unittest

from collections import Counter, deque, namedtuple
from copy import deepcopy
from functools import reduce
from typing import Any


MAZES = [
    (
        {
            'maze': [
                [0, 0, 0],
                [0, 0, 0]
            ],
            'start': (0, 0),
            'end': (1, 2)
        },
        False
    ),
    (
        {
            'maze': [
                [0, 1, 1, 1, 1, 1],
                [1, 1, 0, 0, 0, 1],
                [1, 1, 1, 1, 0, 1],
                [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1]
            ],
            'start': (2, 1),
            'end': (4, 3)
        },
        [(2, 1), (1, 1), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (4, 4), (4, 3)]
    ),
    (
        {
            'maze': [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
                [0, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ],
            'start': (1, 3),
            'end': (4, 7)
        },
        [(1, 3), (1, 2), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
    ),
    (
        {
            'maze': [
                [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
                [1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1],
                [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
                [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
            ],
            'start': (9, 0),
            'end': (0, 14)
        },
        [
            (9, 0), (8, 0), (7, 0), (7, 1), (7, 2), (6, 2), (6, 3), (6, 4), (6, 5), (5, 5), (4, 5), (4, 6), (4, 7),
            (3, 7), (3, 8), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (1, 14), (0, 14)
        ]
    ),
    (
        {
            'maze': [
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0],
                [0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
                [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0],
                [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
                [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
                [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1]
            ],
            'start': (7, 6),
            'end': (5, 18)
        },
        [
            (7, 6), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (2, 5), (1, 5), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9),
            (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (1, 14), (2, 14), (2, 15), (2, 16), (3, 16), (4, 16),
            (5, 16), (6, 16), (6, 17), (6, 18), (5, 18)
        ]
    )
]


class AlgorithmTest(unittest.TestCase):
    algorithm_name: str
    input_args: dict
    expected_output: Any

    def __init__(self, *args, algorithm_name=None, input_args=None, expected_output=None):
        super().__init__(*args)
        self.algorithm_name = algorithm_name
        self.input_args = input_args
        self.expected_output = expected_output

    def test_algorithm_input_output(self):
        algorithm = globals()[self.algorithm_name]

        output = algorithm(**self.input_args)
        self.assertEqual(
            output,
            self.expected_output,
            "\nComputed output: {0}\nExpected output: {1}".format(output, self.expected_output)
        )

    def test_maze_algorithm(self):
        algorithm = globals()[self.algorithm_name]

        output = algorithm(**self.input_args)

        if not self.expected_output:
            self.assertFalse(output)

        else:
            self.assertIsInstance(output, list)
            self.assertEqual(len(output), len(self.expected_output))
            self.assertEqual(output[0], self.input_args['start'])
            self.assertEqual(output[-1], self.input_args['end'])

            prev_x, prev_y = None, None
            for x, y in output:
                if prev_x and prev_y:
                    self.assertEqual((x - prev_x)**2 + (y-prev_y)**2, 1)

                self.assertEqual(self.input_args['maze'][x][y], 1)
                prev_x, prev_y = x, y


def is_anagram(s1, s2):
    """
    Write an algorithm that returns whether s1 and s2 are anagrams of each other, i.e.
    if s1 and s2 contain the same letters in a possibly different order.
    E.g.: "abc" and "cab" are anagrams, "aab" and "bba" are not.
    :param s1: string
    :param s2: string
    :return: True or False
    """

    if len(s1) != len(s2):
        return False

    # find a difference in the distribution of letters
    diff = Counter(s1) - Counter(s2)
    return not diff


def check_parenthesis_consistency(string):
    """
    Write an algorithm that determines if the parenthesis (round brackets "()") in a string are properly balanced.
    An expression is said to be properly parenthesised if it has the form "(p)" or "pq", where p and q are
    properly parenthesised expressions. Any string (including an empty string) that does not contain any parenthesis
    is properly parenthesised.
    E.g.: "()()" is properly parenthesised, "(()" is not.
    :param string: the string to analyse.
    :return: True if the parentheses are balanced, False if not.
    """

    symmetric = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    left_brackets = set(symmetric.keys())
    right_brackets = set(symmetric.values())

    opening_brackets = []
    for character in string:
        # keep order of opening brackets
        if character in left_brackets:
            opening_brackets.append(character)

        # test the correct use of brackets
        elif character in right_brackets:
            if not opening_brackets:
                return False

            opening_bracket = opening_brackets.pop()
            if character != symmetric[opening_bracket]:
                return False

    return not opening_brackets


def shortest_path(start, end, maze):
    """
    Write an algorithm that finds the shortest path in a maze from start to end
    The maze is represented by a list of lists containing 0s and 1s:
    0s are walls, paths cannot go through them
    The only movements allowed are UP/DOWN/LEFT/RIGHT
    :param start: tuple (x_start, y_start) - the starting point
    :param end: tuple (x_end, y_end) - the ending point
    :param maze: list of lists - the maze
    :return: list of positions [(x1, y1), (x2, y2), ...] representing the shortest path in the maze
    """

    # invalid departure or arrival points
    if maze[start[0]][start[1]] == 0 or maze[end[0]][end[1]] == 0:
        return False

    Point = namedtuple('Point', ('x', 'y'))
    START, END = Point(start[0], start[1]), Point(end[0], end[1])
    UP, DOWN, LEFT, RIGHT = Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)
    AUTHORIZED_MOVEMENTS = (UP, DOWN, LEFT, RIGHT)

    maze_copy = deepcopy(maze)  # copy to keep the original maze untouched
    queue = deque()  # the sequence of points to be explored
    prev = {}  # log the previous point, to keep records of movements

    maze_copy[START.x][START.y] = 0  # mark the starting point as visited
    queue.append((START, 0))  # adding the starting point with the number of steps from the starting point
    while queue:
        cursor, step = queue.popleft()

        if cursor == END:  # the target is reached, get the shortest path from "start" to "end"
            return reduce(lambda path, _: [prev[path[0]]] + path, range(step), [END])

        for move in AUTHORIZED_MOVEMENTS:
            neighbour = Point(cursor.x + move.x, cursor.y + move.y)

            try:  # Assessing the next move
                assert neighbour.x >= 0 and neighbour.y >= 0
                assert maze_copy[neighbour.x][neighbour.y] == 1

            except (AssertionError, IndexError):
                continue

            else:
                maze_copy[neighbour.x][neighbour.y] = 0  # mark the cell as visited
                queue.append((neighbour, step + 1))  # next point to check
                prev[neighbour] = cursor  # log the previous point

    return False


if __name__ == "__main__":
    suite = unittest.TestSuite()

    for inp, out in (({"s1": "pouet", "s2": "prout"}, False), ({"s1": "abc", "s2": "bca"}, True),
                     ({"s1": "abbc", "s2": "bcba"}, True), ({"s1": "abbc", "s2": "cba"}, False),
                     ({"s1": "abbc", "s2": ""}, False), ({"s1": "", "s2": ""}, True)):
        suite.addTest(AlgorithmTest(
            "test_algorithm_input_output",
            algorithm_name="is_anagram",
            input_args=inp,
            expected_output=out
        ))

    for inp, out in (("()", True), ("(())", True), ("()()", True), ("(()", False), ("())", False),
                     ("(((()", False), ("())))", False)):
        suite.addTest(AlgorithmTest(
            "test_algorithm_input_output",
            algorithm_name="check_parenthesis_consistency",
            input_args={
                "string": inp
            },
            expected_output=out
        ))

    for inp, out in MAZES:
        suite.addTest(AlgorithmTest(
            "test_maze_algorithm",
            algorithm_name="shortest_path",
            input_args=inp,
            expected_output=out
        ))

    runner = unittest.TextTestRunner()
    runner.run(suite)

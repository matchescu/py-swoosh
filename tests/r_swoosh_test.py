from typing import Iterable

import pytest

from stanford_swoosh.swoosh import r_swoosh


def test_r_swoosh_integer_numbers():
    result = r_swoosh([1], lambda x, y: x%2 == 1, lambda x, y: x+y)

    assert result == [1]


@pytest.fixture
def students_table():
    return [
        ["Edgar", "Jones", 20001104, "G34"],
        ["Mary", "Smith", 19990921, "G55"],
        ["Eddie", "Jones", 20001104, "G34"],
        ["Mary", "Smith", 19990921, "H17"],
        ["Eddie", "Jones", 20001104, "H15"],
    ]


def compare_tuples(a, b):
    return a[1] == b[1] and a[2] == b[2]


def merge_tuples(a, b):
    i = 0
    n = min(map(len, [a, b]))

    def _build_set(x):
        if isinstance(x, set):
            for val in x:
                element_set.add(val)
        else:
            element_set.add(x)

    result = []

    while i < n:
        if a[i] == b[i]:
            result.append(a[i])
        else:
            element_set = set()
            _build_set(a[i])
            _build_set(b[i])
            result.append(element_set)
        i += 1

    return result


def test_r_swoosh_students(students_table):
    result = r_swoosh(students_table, compare_tuples, merge_tuples)

    assert result == [
        ["Mary", "Smith", 19990921, {"G55", "H17"}],
        [{"Edgar", "Eddie"}, "Jones", 20001104, {"G34", "H15"}],
    ]

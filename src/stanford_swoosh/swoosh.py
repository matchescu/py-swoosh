from typing import Callable, Any, Iterable


def r_swoosh(data: list, match: Callable[[Any, Any], bool], merge: Callable[[Any, Any], Any]) -> list:
    buf = data
    er = list()
    i = 0
    j = 0
    while i < len(data):
        x = buf[i]
        if j >= len(er):
            er.append(x)
            buf.pop(i)
            j = 0
            continue
        y = er[j]
        if match(x, y):
            z = merge(x, y)
            er.pop(j)
            buf.pop(i)
            buf.append(z)
            continue
        else:
            j += 1
    return er

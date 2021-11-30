from math import sqrt


def mean(lst):
    s = 0
    for val in lst:
        s += val
    return s / len(lst)


def median(lst):
    return mean(sorted(lst)[(len(lst) - 1) // 2: len(lst) // 2 + 1])


def std(lst):
    m = mean(lst)
    return sqrt(mean([(val - m) ** 2 for val in lst]))

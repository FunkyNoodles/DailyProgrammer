import numpy as np
import itertools


def parse_input(_file_name):
    n_flag = False
    _arr = []
    _n = 0
    with open(_file_name, 'r') as f:
        for line in f:
            for s in line.split(' '):
                num = int(s)
                if not n_flag:
                    _n = num
                    n_flag = True
                    break
                _arr.append(num)

    return _n, _arr


def seen_buildings(permutation, _n):
    max_height = -1
    count = 0
    for i in permutation:
        if i > max_height:
            max_height = i
            count += 1
    if count == _n:
        return 0
    return count


def build_combinations(_n):
    _combinations_map = {}
    numbers = range(0, _n)
    for i in numbers:
        _combinations_map[i] = []
    permutations = itertools.permutations(numbers)
    for p in permutations:
        _arr = list(p)
        # print _arr, seen_buildings(_arr, _n)
        _combinations_map[seen_buildings(_arr, _n)].append(_arr)
    return _combinations_map

file_name = 'input1'

n, arr = parse_input(file_name)
grid = np.zeros(shape=[n, n], dtype=int)
combinations = build_combinations(3)


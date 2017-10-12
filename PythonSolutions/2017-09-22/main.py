import numpy as np
import itertools
import time


class Index:
    index = 0
    requirement = 0
    def __init__(self, _index, _requirement):
        self.index = _index
        self.requirement = _requirement

    def __lt__(self, other):
        return self.requirement < other.requirement

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

def seen_buildings(permutation):
    max_height = -1
    count = 0
    for _i in permutation:
        if _i > max_height:
            max_height = _i
            count += 1
    return count

def build_combinations(_n):
    _combinations_map = {}
    for _i in range(0, _n + 1):
        _combinations_map[_i] = []
    permutations = itertools.permutations(range(1, _n + 1))
    for p in permutations:
        _arr = list(p)
        _combinations_map[seen_buildings(_arr)].append(_arr)
    for k, v in _combinations_map.iteritems():
        _combinations_map[0] += v
    return _combinations_map

def try_place(_index, _candidate, _n, _grid):
    new_grid = np.array(_grid)
    region = _index / _n
    sub_index = _index % _n
    if region == 0:
        # Vertical down
        for i in range(0, _n):
            _c = _candidate[i]
            if _c != _grid[i, sub_index] and _grid[i, sub_index] != 0:
                return None
            new_grid[i, sub_index] = _c
    elif region == 1:
        # Horizontal left
        for j in range(0, _n):
            _c = _candidate[_n - j - 1]
            if _c != _grid[sub_index, j] and _grid[sub_index, j] != 0:
                return None
            new_grid[sub_index, j] = _c
    elif region == 2:
        # Vertical up
        for i in range(0, _n):
            _c = _candidate[i]
            if _c != _grid[_n - 1 - i, _n - 1 - sub_index] and _grid[_n - 1 - i, _n - 1 - sub_index] != 0:
                return None
            new_grid[_n - 1 - i, _n - 1 - sub_index] = _c
    elif region == 3:
        # Horizontal right
        for j in range(0, _n):
            _c = _candidate[j]
            if _c != _grid[_n - 1 - sub_index, j] and _grid[_n - 1 - sub_index, j] != 0:
                return None
            new_grid[_n - 1 - sub_index, j] = _c

    return new_grid

def solve(_index, _grid, _n, _options, _arr, _combinations):
    for _candidate in _options:
        new_grid = try_place(_arr[_index].index, _candidate, _n, _grid)
        # print new_grid, _index
        if new_grid is None:
            continue
        if _index == _n * 4 - 1:
            # Found solution
            return new_grid
        next_options = _combinations[_arr[_index + 1].requirement]
        print new_grid
        _solved_grid = solve(_index + 1, new_grid, _n, next_options, _arr, _combinations)
        if _solved_grid is not None:
            return _solved_grid

    return None


file_name = 'input4'

n, arr = parse_input(file_name)
index_arr = [Index(idx, req) for idx, req in enumerate(arr)]
index_arr = sorted(index_arr, reverse=True)

start = time.time()
combinations = build_combinations(n)
# print combinations

solved_grid = solve(0, np.zeros(shape=[n, n], dtype=int), n, combinations[index_arr[0].requirement], index_arr, combinations)
print solved_grid
end = time.time()
print 'Took:', (end - start), 's'

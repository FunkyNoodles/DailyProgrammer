import numpy as np
import itertools
import time


class Index:
    index = 0
    requirement = 0
    combinations = {}
    def __init__(self, _index, _requirement, _combinations):
        self.index = _index
        self.requirement = _requirement
        self.combinations = _combinations

    def __lt__(self, other):
        return len(self.combinations[self.requirement]) < len(other.combinations[other.requirement])


def parse_input(_file_name):
    n_flag = False
    _arr = []
    _n = 0
    _init_grid = None
    with open(_file_name, 'r') as\
            f:
        for _index, line in enumerate(f):
            for _j, s in enumerate(line.split(' ')):
                num = int(s)
                if _index < 2:
                    if not n_flag:
                        _n = num
                        _init_grid = np.zeros(shape=[_n, _n], dtype=int)
                        n_flag = True
                        break
                    _arr.append(num)
                else:
                    _init_grid[_index - 2, _j] = num

    return _n, _arr, _init_grid

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
    permutations = itertools.permutations(list(range(1, _n + 1)))
    for p in permutations:
        _arr = list(p)
        _combinations_map[seen_buildings(_arr)].append(_arr)
    for k, v in _combinations_map.items():
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
                # Cannot place because overlap
                return None
            perpendicular = _grid[i, :]
            perpendicular = np.delete(perpendicular, sub_index)
            if _c in perpendicular:
                # Cannot place because already exists
                return None
            new_grid[i, sub_index] = _c
    elif region == 1:
        # Horizontal left
        for j in range(0, _n):
            _c = _candidate[_n - j - 1]
            if _c != _grid[sub_index, j] and _grid[sub_index, j] != 0:
                return None
            perpendicular = _grid[:, j]
            perpendicular = np.delete(perpendicular, sub_index)
            if _c in perpendicular:
                # Cannot place because already exists
                return None
            new_grid[sub_index, j] = _c
    elif region == 2:
        # Vertical up
        for i in range(0, _n):
            _c = _candidate[i]
            if _c != _grid[_n - 1 - i, _n - 1 - sub_index] and _grid[_n - 1 - i, _n - 1 - sub_index] != 0:
                return None
            perpendicular = _grid[_n - 1 - i, :]
            perpendicular = np.delete(perpendicular, _n - 1 - sub_index)
            if _c in perpendicular:
                # Cannot place because already exists
                return None
            new_grid[_n - 1 - i, _n - 1 - sub_index] = _c
    elif region == 3:
        # Horizontal right
        for j in range(0, _n):
            _c = _candidate[j]
            if _c != _grid[_n - 1 - sub_index, j] and _grid[_n - 1 - sub_index, j] != 0:
                return None
            perpendicular = _grid[:, j]
            perpendicular = np.delete(perpendicular, _n - 1 - sub_index)
            if _c in perpendicular:
                # Cannot place because already exists
                return None
            new_grid[_n - 1 - sub_index, j] = _c

    return new_grid

def solve(_index, _grid, _n, _options, _arr, _combinations, _nodes_expanded):
    for _candidate in _options:
        _nodes_expanded += 1
        new_grid = try_place(_arr[_index].index, _candidate, _n, _grid)
        if new_grid is None:
            continue
        if _index == _n * 4 - 1:
            # Found solution
            return new_grid, _nodes_expanded
        next_options = _combinations[_arr[_index + 1].requirement]
        print(new_grid, _index)
        _solved_grid, _nodes_expanded = solve(_index + 1, new_grid, _n, next_options, _arr, _combinations, _nodes_expanded)
        if _solved_grid is not None:
            return _solved_grid, _nodes_expanded

    return None, _nodes_expanded


file_name = 'input3'

n, arr, init_grid = parse_input(file_name)

start = time.time()
combinations = build_combinations(n)

index_arr = [Index(idx, req, combinations) for idx, req in enumerate(arr)]
index_arr = sorted(index_arr)
# for i in index_arr:
#     print i.index, i.requirement
#
# for k, v in combinations.iteritems():
#     print k, len(v)

solved_grid, nodes_expanded = solve(0, init_grid, n, combinations[index_arr[0].requirement], index_arr, combinations, 0)
print(solved_grid)
end = time.time()
print('Took:', (end - start), 's', '\tNodes Expanded:', nodes_expanded)

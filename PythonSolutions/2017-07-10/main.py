import itertools

numbers_string = input('List of integers:\n')
numbers = [int(s) for s in numbers_string.split(' ')]

for subset in itertools.combinations(numbers, 3):
    if sum(subset) == 0:
        print(subset)


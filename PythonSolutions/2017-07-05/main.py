import time


def is_palindrome(string):
    for idx, char in enumerate(string):
        if char != string[-idx-1]:
            return False
    return True

n = input('n:\n')
max_factor_i = 0
max_factor_j = 0
max_product = 0

found = False

start = time.time()

for i in reversed(range(1, 10**n)):
    if len(str(i)) < n or found:
        break

    for j in reversed(range(1, i+1)):
        if len(str(j)) < n:
            break
        product = i * j
        if i < max_factor_i and j < max_factor_j:
            found = True
            break
        if product < max_product:
            break
        if is_palindrome(str(product)):
            if product > max_product:
                max_factor_i = i
                max_factor_j = j
                max_product = product

end = time.time()
print max_product, 'factors:', max_factor_i, 'and', max_factor_j
print 'Took', end - start, 's'

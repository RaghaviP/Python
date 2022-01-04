from functools import reduce

list_ints = [1, 2, 3, 4, 5, 6]

total = reduce(lambda x, y: x + y, list_ints)

print(f'sum of list_ints elements is {total}')





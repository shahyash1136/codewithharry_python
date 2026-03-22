# 6. map(), filter(), and reduce()
# 1. Use  map()  to convert  [1, 2, 3, 4, 5]  into their cubes.
# 2. Use  filter()  to get only even numbers from  [10, 11, 12, 13, 14] .
# 3. Use  reduce()  from  functools  to find the product of all elements in  [1, 2,3, 4]

map_number = [1, 2, 3, 4, 5]
update_map_number = list(map(lambda x: x**3, map_number))
print(update_map_number)

filter_number = [10, 11, 12, 13, 14]
updated_filter_number = list(filter(lambda x: x % 2 == 0, filter_number))
print(updated_filter_number)

from functools import reduce

number = [1, 2, 3, 4]


def product(a, b):
    return a * b


print(reduce(product, number))

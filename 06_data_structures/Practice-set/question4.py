# 4. Sets and Set Methods
# 1. Create a set  my_set = {1, 2, 3, 3, 4}  and print it. (What happens to duplicate  3 ?)
my_set = {1, 2, 3, 3, 4} # only a single 3 is printed
print(my_set) 
# 2. Add  5  to the set, remove  2 , and check if  4  is in the set.
my_set.add(5)
my_set.remove(2)
print("4 in set:", 4 in my_set)
print(my_set)

# 3. Create two sets:
#     a. a = {1, 2, 3}
#     b. b = {3, 4, 5} Find their:
#     c. Union
#     d. Intersection
#     e. Difference ( a - b )
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# 3. Lambda Functions
# 1. Write a lambda function that adds two numbers and test it.
sum = lambda x, y: x + y
print(sum(2,3))

# 2. Create a list  [1, 2, 3, 4, 5]  and use  map()  with a lambda function to get their squares.
data = [1, 2, 3, 4, 5]
square = list(map(lambda x : x**2,data))
print(square)

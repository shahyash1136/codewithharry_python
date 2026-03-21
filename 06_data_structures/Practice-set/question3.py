# 3. Tuples and Operations on Tuples
# 1. Create a tuple  coordinates = (10, 20)  and print both elements.
coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

# 2. Try to modify the tuple by setting  coordinates[0] = 50  — note what happens.
# coordinates[0] = 50  # Throws error 'tuple' object does not support item assignment
# print(coordinates)

# 3. Convert the tuple to a list, change its first element to  50 , and convert it back to a tuple.
updateCoordinates = list(coordinates)
updateCoordinates[0] = 50
updateCoordinates = tuple(updateCoordinates)
print(updateCoordinates)
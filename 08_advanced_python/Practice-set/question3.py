# 3. Static & Class Methods
# 1. Create a class  MathUtils  with:
#     a. A  @staticmethod  called  add(a, b)  that returns  a + b .
#     b. A  @classmethod  called  description(cls)  that prints  "This is a utility class for math operations."
# 2. Call both methods without creating an object.
class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return print("This is a utility class for math operations.")


print(MathUtils.add(2, 3))
MathUtils.description()

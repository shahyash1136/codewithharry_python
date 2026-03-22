# 2. Getters and Setters
# 1. Create a class  Employee  with a private attribute  _salary .
#     a. Use  @property  to define a getter for  salary .
#     b. Use  @salary.setter  to prevent setting negative values (print a warning instead).
#     c. Create an object and test by setting positive and negative salaries.
class Employee:
    def __init__(self, salary):
        self._salary_value = salary

    @property
    def salary(self):
        return self._salary_value

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            print("Salary cannot be negative")
            return
        self._salary_value = salary


e1 = Employee(10000)
print(e1.salary)
e1.salary = -5000
print(e1.salary)
e1.salary = 15000
print(e1.salary)

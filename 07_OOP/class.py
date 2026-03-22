# Class : Class is a blueprint or a template. Eg. Form for an Exam that contains name, age, electives, father's name etc

# Object: Specific instance creted from the template (class.). Eg. From which contains the data for John Doe


class Employee:
    company = "HP"

    def get_salary(
        self,
    ):  # self is important here because self is a way to reference the object of the class which is being created
        return 34000


emp1 = Employee()  # An object of class employeee is created
print(emp1.get_salary())  # Employee emp1 get salary method is called

emp2 = Employee()
print(emp2.get_salary())
print(emp1.company)
print(emp2.company)

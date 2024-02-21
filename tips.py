

class Employee:
    def __init__(self,name, salary):
        self.name =name
        self.salary = salary

emp = Employee("Ahmed", 299)
print(emp)
print(emp.__dict__)
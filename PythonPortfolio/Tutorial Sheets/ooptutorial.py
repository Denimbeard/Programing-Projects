# Classes are blueprints that make instances of a class

# emp_1 = Employee()
# emp_2 = Employee()

# These two things become independant objects or 'instances'

"""
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Corey'
emp_2.last = 'Schafer'
emp_2.email = 'Corey.Schafer@company.com'
emp_2.pay = 50000
"""

# these are the same details for different instances
# and can be performed with a class

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return('{} {}'.format(self.first, self.last))

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(Employee.fullname(emp_1))
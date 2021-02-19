# python Object-Oriented Programing
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

Creating Classes:
Why Use Classes?
Classes allow us to logically group data and functions for reuse and addition.
Method: a function associated with a class.

Ex:
Employees in buiness database
class Employee:
    pass -> tells python to skip the object

instance of a class vs class
classes are the blue print, each employee is the instance

emp_1 = Employee()
emp_2 = Employee()

these are both valid objects using the class as a format

instance variables contain data unique to each instance

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = email
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'user'
emp_2.email = email
emp_2.pay = 60000

Manually setting these variables each time is prone to errors, instead set the class to define them.

class Employee:
    def __init__(self -> the initial instance is self
                 first,
                 last,
                 pay
                    ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'companyname.com'

'self' is automatic, so leave it off in the definition

emp_1 = Employee('Corey', Schafer', 50000)
class will automatically set:
    emp_1.first = 'Corey'
    emp_1.last = 'Schafer'
    emp_1.email = email
    emp_1.pay = 50000

emp_2 = Employee('Test', 'User', 60000)
    emp_2.first = 'Test'
    emp_2.last = 'user'
    emp_2.email = email
    emp_2.pay = 60000

setting functions outside of the class is allowed
setting functions inside is allowed as well

class Employee:
    def __init__(self -> the initial instance is self
                 first,
                 last,
                 pay
                    ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'companyname.com'

    def fullname(self): -> using self allows for multiple instances
        return '{} {}.format(self.first, self.last)

print(emp_1.fullname())
    returns Corey Shafer

Do not forget the self indicator in the class method
instance.fullname() -> instance will be ran through the method

These are the same thing:
1. emp_1.fullname()
2. print(Employee.fullname(emp_1))

so use the first one to save time and code

# https://www.youtube.com/watch?v=BJ-VvGyQxho

class variables are variables that are shared over all instances of that class

class Employee:
    def __init__(self -> the initial instance is self
                 first,
                 last,
                 pay
                    ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'companyname.com'

    def fullname(self): -> using self allows for multiple instances
        return '{} {}.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
    
emp_1.apply_raise() -> will now do the math for the raise

setting the raise ammount as a class variable will clean up the code!

class Employee:
    
    raise_amount = 1.04

    def __init__(self -> the initial instance is self
                 first,
                 last,
                 pay
                    ):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'companyname.com'

    def fullname(self): -> using self allows for multiple instances
        return '{} {}.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

        
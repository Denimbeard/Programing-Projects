# Python Classes and Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with it's properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

#To create a class, use the keyword class:

class MyClass:
    x = 5

# Now we can use the class named MyClass to create objects.
# Create an object named p1 and print the value of x

p1 = MyClass()
print(p1.x)

# The examples above are classes and objects in their simplest form,
# and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the
# __init__() function.

# All classes have a function called __init__(), which is always
# executed when the class is being initiated.

# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Objects can also contain methods. Methods in objects are functions
# that belong to the object.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Note: The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.

# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.

# It does not have to be named self ,
# you can call it whatever you like,
# but it has to be the first parameter of any function in the class:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Sets the age of the p1 to 40
p1.age = 40

# Delete the age property from the p1 object
del p1.age

# Delete the p1 object
del p1

# Class definitions cannot be empty, but if you for some reason
# have a class definition with no content, put in the pass statement
# to avoid getting an error.

class Person:
    pass

# Inheritance allows us to define a class that inherits all the methods and properties
# from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class:

# Create a class named Student, which will inherit the properties
# and methods from the Person class:

class Student(Person):
  pass

# Note: Use the pass keyword when you do not want to add any other properties
# or methods to the class.

# Now the Student class has the same properties and methods as the Person class.

x = Student("Mike", "Olsen")
x.printname()

# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

# When you add the __init__() function, the child class will no longer
# inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the
# parent's __init__() function.

# To keep the inheritance of the parent's __init__() function,
# add a call to the parent's __init__() function:

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# Now we have successfully added the __init__() function,
# and kept the inheritance of the parent class,
# and we are ready to add functionality in the __init__() function.

# Python also has a super() function that will make the child class inherit
# all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# By using the super() function, you do not have to use the name of the parent element,
# it will automatically inherit the methods and properties from its parent.
# Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

# In the example below, the year 2019 should be a variable,
# and passed into the Student class when creating student objects.
# To do so, add another parameter in the __init__() function:

# Add a year perameter and pass the correct year when creating objects:

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)

# Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# If you add a method in the child class with the same name as a function in the parent class,
# the inheritance of the parent method will be overridden.

# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

# Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# Iterate the characters of a string:
mystr = "banana"

for x in mystr:
  print(x)

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(),
# which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.),
# but must always return the iterator object itself.
# The __next__() method also allows you to do operations,
# and must return the next item in the sequence.

# Create an iterator that returns numbers, starting with 1,
# and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration to go on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition
# to raise an error if the iteration is done a specified number of times:

# Stop after 20 iterations:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x<>>>

    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


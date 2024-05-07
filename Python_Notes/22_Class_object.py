# Class:
# A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

# Object:
# Object is the instance of the class used to access the properties of the class Now lets create an object of the class.

# Self parameter:
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.

# 1.
class Details: #For creating Class
    name = "Ritesh"
    age = 20
obj1 = Details() #For creating object
print(obj1.name) 
print(obj1.age)


# 2.
class Person: #For creating Class
  name = "Harry"
  occupation = "Software Developer"
  networth = 10

  def info(self): #For creating function
    print(f"{self.name} is a {self.occupation}") # Use of f string


a = Person() #For creating object
b = Person() #For creating object
c = Person() #For creating object

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika" 
b.occupation = "HR"
# print(a.name, a.occupation)
a.info()
b.info()
c.info()
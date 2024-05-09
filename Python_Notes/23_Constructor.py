# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# Syntax :
#   def __init__(self):
    # initializations


# Types of Constructors in Python :
# 1. Parameterized Constructor
# 2. Default Constructor

# Parameterized Constructor in Python :
# When the constructor accepts arguments along with self, it is known as parameterized constructor.

class anime:
    def __init__(self,name,ep):
        self.name=name
        self.ep=ep
obj1 = anime("Onepiece",1103) 
print("Example of Parameterized Contructor")
print("I have watched", obj1.ep ,"of",obj1.name,"\n" ) 


# Default Constructor in Python
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it is known as a Default constructor.
class Details:
  def __init__(self):
    print("\nExample of Default Contructor")
    print("animal Crab belongs to Crustaceans group")
obj1=Details()
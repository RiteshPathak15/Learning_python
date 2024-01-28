# Docstrings in python
# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
# Python doc attribute
# Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. 
# We can later use this attribute to retrieve this docstring.

# Example:
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) #used to print docString 


# PEP 8:

# PEP 8 is a document that provides guidelines and best practices on how to write Python code.
# It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. 
# The primary focus of PEP 8 is to improve the readability and consistency of Python code.
# PEP stands for Python Enhancement Proposal, and there are several of them.
# A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.
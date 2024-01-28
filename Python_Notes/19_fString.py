# String formatting in python
# String formatting can be done in python using the format method.

# Without F-String:
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"
print(letter.format(country, name))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# With F-String:
# f-strings in python
# It is a new string formatting mechanism introduced by the PEP 498.
#  It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal).
#  The primary focus of this mechanism is to make the interpolation easier.
# When we prefix the string with the letter 'f', the string becomes the f-string itself. 
# The f-string can be formatted in much same as the str.format() method. 
# The f-string offers a convenient way to embed Python expression inside string literals for formatting.

# Example:
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Ritesh"
print(f"Hey my name is {name} and I am from {country}")


val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Ritesh'  
age = 20  
print(f"Hello, My name is {name} and I'm {age} years old.")

# With {{ }} in F-String:
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
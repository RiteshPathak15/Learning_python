# Python string is the collection of the characters surrounded by single quotes, double quotes, or triple quotes.
str = "Hi Python !"    
print(type(str))

#Using single quotes  
str1 = 'Hello Python'  
print(str1)  
#Using double quotes  
str2 = "Hello Python"  
print(str2)   
#Using triple quotes  
str3 = '''''Triple quotes are generally used for  
    represent the multiline or 
    docstring'''   
print(str3)  

# Strings indexing and splitting
# ->->->->->->->->->->->->->->->->->->->->->->->->->
#       0         1         2         3        4
#     | H   |     E    |    L    |    L  |     O   |
#      -5        -4        -3        -2        -1
# ===========================

str = "HELLO"  
print(str[0])  
print(str[1])  
print(str[2])  
print(str[3])  
print(str[4])  
# It returns the IndexError because 6th index doesn't exist  
# print(str[6])  //it will show error because there is index 6 present str 


# Looping through the string
for character in str:
    print(character)


# String Slicing & Operations on String
# Length of a String
name = "Ritesh"
len1 = len(name)
print("Ritesh is a", len1, "letter word.")

# String as an array
pie = "Ritesh_Pathak"
print(pie[:5])
print(pie[6])	#returns character at specified index

# Given String  
str = "Ritesh Pathak"  
# Start Oth index to end  
print(str[0:])  
# Starts 1th index to 4th index  
print(str[1:5])  
# Starts 2nd index to 3rd index  
print(str[2:4])  
# Starts 0th to 2nd index  
print(str[:3])  
#Starts 4th to 6th index  
print(str[4:7])  

str = 'Ritesh_Pathak'  
print(str[-1])  
print(str[-3])  
print(str[-2:])  
print(str[-4:-1])  
print(str[-7:-2])  
# Reversing the given string  
print(str[::-1])  
print(str[-12])  


#string Methods
# Example:

str1 = "Ritesh_Pathak"

# upper() : The upper() method converts a string to upper case.
print(str1.upper())

#lower(): The lower() method converts a string to lower case.
print(str1.lower())

# strip() :The strip() method removes any white spaces before and after the string.
print(str2.strip)

# rstrip() :the rstrip() removes any trailing characters. Example:
print(str3.rstrip("!"))

# replace() : The replace() method replaces all occurences of a string with another string. Example:
print(str2.replace("Pa", "pa"))

# split() : The split() method splits the given string at the specified instance and returns the separated strings as list items.
print(str2.split(" "))      #Splits the string at the whitespace " ".

# capitalize() :The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)

# center() :The center() method aligns the string to the center as per the parameters given by the user.
print(str1.center(50))
# -----------------OR--------------------------------
# We can also provide padding character. It will fill the rest of the fill characters provided by the user.
str2 = "Welcome to the Console!!!"
print(str2.center(50, "."))

# count() :The count() method returns the number of times the given value has occurred within the given string.
countStr = str1.count("a")
print(countStr)

# endswith() :The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
print(str1.endswith("!!!"))

# find() :The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
str3 = "He's name is Dan. He is an honest man."
print(str3.find("is"))

# index() :The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
print(str3.index("Dan"))

# isalnum() :The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
print(str1.isalnum())

# isalpha() :The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
print(str1.isalpha())

# islower() :The islower() method returns True if all the characters in the string are lower case, else it returns False.
print(str1.islower())

# isupper() :The isupper() method returns True if all the characters in the string are upper case, else it returns False.
print(str1.isupper())

# startswith() :The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
str4 = "Python is a Interpreted Language" 
print(str4.startswith("Python"))


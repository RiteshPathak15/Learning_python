# Python Dictionaries
# Dictionaries are ordered collection of data items. 
#They store multiple items in a single variable. 
#Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Accessing Dictionary items:
# I. Accessing single values:

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))

# II. Accessing multiple values:
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# III. Accessing keys:
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# IV. Accessing key-value pairs:
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())


# Dictionary Methods: Dictionary uses several built-in methods for manipulation.They are listed below

# update(): The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

# Removing items from dictionary:
# clear(): The clear() method removes all the items from the list.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

# pop(): The pop() method removes the key-value pair whose key is passed as a parameter.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

# popitem(): The popitem() method removes the last key-value pair from the dictionary.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

# del: We can also use the del keyword to remove a dictionary item.
# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

# Example:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)

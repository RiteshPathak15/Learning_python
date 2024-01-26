# Python Sets
# Sets are unordered collection of data items. 
#They store multiple items in a single variable. 
#Set items are separated by commas and enclosed within curly brackets {}. 
#Sets are unchangeable, meaning you cannot change items of the set once created. 
#Sets do not contain duplicate items.

# Example:
info = {"Carla", 19, False, 5.9, 19}
print(info)

# Accessing set items:
# Using a For loop
# Example:
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)

# Set Methods
# There are several in-built methods used for the manipulation of set.They are explained below

# isdisjoint(): The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# issuperset(): The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

# issubset(): The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add():If you want to add a single item to the set use the add() method.
# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# update(): If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# remove()/discard():We can use remove() and discard() methods to remove items form list.
# Example :
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)

# pop():This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del : del is not a method, rather it is a keyword which deletes the set entirely.
# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

# clear(): This method clears all items in the set and prints an empty set.
# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# Example
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")

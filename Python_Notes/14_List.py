# Python Lists
# Lists are ordered collection of data items.
# They store multiple items in a single variable.
# List items are separated by commas and enclosed within square brackets [].
# Lists are changeable meaning we can alter them after creation.
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)

# List Index:
# Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.
# ->->->->->->->->->->->->->->->->->->->->->->->->->
#       0         1         2         3        4
# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#      -5        -4        -3        -2        -1
# <-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-<-
# Accessing list items
# We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

# Checking if element is present in the given list or not
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")

# Range of Index:
# Syntax:
# listName[start : end : jumpIndex]\
# Note: jump Index is optional. We will see this in later examples.
# Example: printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'


# Example: printing all element from a given index till the end
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes

# Example: printing all elements from start to a given index
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes

# Example: Printing alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes

# Example: printing every 3rd consecutive value withing a given range
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])


# List Comprehension :
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# Syntax:
# List = [Expression(item) for item in iterable if Condition]
# Expression: It is the item which is being iterated.
# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
# Condition: Condition checks if the item should be added to the new list or not.

# Example 1: Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

# Example 2: Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)



#List Method:

# list.sort(): This method sorts the list in ascending order. The original list is updated
# Example 1:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)

# if you want to print the list in descending order?
# We must give reverse=True as a parameter in the sort method.

# Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
# The reverse parameter is set to False by default.
# Note: Do not mistake the reverse parameter with the reverse method.


# reverse(): This method reverses the order of the list.
# Example:
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)
num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)


# index():This method returns the index of the first occurrence of the list item.
# Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))


# count(): Returns the count of the number of items with the given value.
# Example:
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]


# copy(): Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
# Example:
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

# append():This method appends items to the end of the existing list.
# Example:
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)


# insert(): This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
# Example:
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]
colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]
print(colors)


# extend(): This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
# Example 1:
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)


# Concatenating two lists:
# You can simply concatenate two lists to join two lists.
# Example:
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)

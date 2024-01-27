# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.
point=1
total_points = 0
print("What is the correct way to calculate the length of a list in Python?")
option1=["a.len(list_length)", "b.list.size()", "c.list.len()", "d.len(list)"]
print(option1)
Ans1="d"
a="D"
a1="d.len(list)"

answer1=input("Enter the Answer you thing is write: ")
if answer1==Ans1 or answer1==a or answer1==a1:
    print("You Have Entered the write Ans")
    total_points=total_points+point

else:
    print("\nYou Have Entered the wrong value\nWrite Answer:d.len(list)")

if answer1==Ans1 or answer1==a or answer1==a1:
    print("Your Points: ",point)

    

print(" ")

print("In Python, which of the following is used to comment a single line of code?")
option2=["a./* */","b.//","c.#","d.<!-- -->"]
print(option2)
a="c"
a2="C"
Ans2="c.#"
answer2=input("Enter the Answer you thing is write: ")
if answer2==Ans2 or answer2==a or answer2==a2:
    print("You Have Entered the write Ans")
    total_points+=point
else:
    print("You Have Entered the wrong value\nWrite Answer:c.#")

if answer2==Ans2 or answer2==a or answer2==a2:
    print("Your Points: ",point)



print(" ")

print("How can you check if a key is present in a dictionary in Python?")
option3=["a.key in dictionary","b.dictionary.key()","c.key.exists(dictionary)","d.dictionary.contains(key)"]
print(option3)
Ans3="a.key in dictionary"
a="a"
a3="A"
answer3=input("Enter the Answer you thing is write: ")
if answer3==Ans3 or answer3==a or answer3==a3:
    print("You Have Entered the write Ans")
    total_points+=point
else:
    print("You Have Entered the wrong value\nWrite Answer:a.key in dictionary")

if answer3==Ans3 or answer3==a or answer3==a3:
    print("Your Points: ",point)



print(" ")

print("Python was created by:")
option4=["a.Guido van Rossum" , "b.Guido von Rossum" ,"c.Vivek" ,"d.Atharv" ,"e.Pradeep"]
print(option4)
Ans4="a.Guido van Rossum"
a="a"
a4="A"
answer4=input("Enter the Answer you thing is write: ")
if answer4==Ans4  or answer4==a or answer4==a4: 
    print("You Have Entered the write Ans")
    total_points+=point
else:
    print("You Have Entered the wrong value\nWrite Answer:a.Guido van Rossum")
    

if answer4==Ans4  or answer4==a or answer4==a4:
    print("Your Points: ",point)


print("Total Points you gained : ", total_points)
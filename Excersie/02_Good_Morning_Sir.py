# <!-- Excersice 2: Good Morning Sir
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you: -->
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print("%H for Hour: ",timestamp)
timestamp = time.strftime('%M')
print("%M for Minute: ", timestamp)
timestamp = time.strftime('%S')
print("%S for second: ", timestamp)
timestamp = time.strftime('%Y')
print("%Y for Year: ", timestamp)
timestamp=time.strftime('%B')
print("%B for Month: ", timestamp)
timestamp=time.strftime("%A")
print("%A for Week: ", timestamp)
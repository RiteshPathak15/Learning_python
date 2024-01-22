# Python break statement
# The break is a keyword in python which is used to bring the program control out of the loop. The break statement breaks the loops one by one, 
# i.e., in the case of nested loops, it breaks the inner loop first and then proceeds to outer loops. 
for multi in range(1,10,1):
    print("Multiplication of 5: ",5*multi)
    if(multi==5):
        print("Break block is excuted")
        break
print("End of the code")



# Python continue Statement
# Python continue keyword is used to skip the remaining statements of the current loop and go to the next iteration.
for multi in range(1,10,1):
    if(multi==5):
        print("Continue block is excuted")
        continue
    print("Multiplication of 5: 5 *",multi ,5*multi)
print("End of the code")
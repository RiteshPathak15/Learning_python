#If Conditional Statment
# The if statement is used to test a specific condition. If the condition is true, a block of code (if-block) will be executed.
# Syntax:
        # if(Condition):
            #Code Statment

sum=int(input("Enter the number :"))
if sum % 2==0:     
    print(sum,"is an Even Number")  


# if-else condition:
#The if-else statement provides an else block combined with the if statement which is executed in the false case of the condition.
# If the condition is true, then the if-block is executed. Otherwise, the else-block is executed.
# Syntax:
        # if(Condition):
            #Code Statment
        # else:
            #code Statement
age=int(input("Enter the age :"))
if age>=18:
    print("Eligible to Vote")
else:
    print("Not Eligible For Voting")



# The elif statement
# The elif statement enables us to check multiple conditions and execute the specific block of statements depending upon the true condition among them.
# Syntax:
    #    if expression 1:   
            # block of statements   
  
        # elif expression 2:   
            # block of statements   
  
        # elif expression 3:   
            # block of statements   
  
        # else:   
            # block of statements
marks = int(input("Enter the marks? "))    
if marks > 85 and marks <= 100:  
   print("Congrats ! you scored grade A ...")    
elif marks > 60 and marks <= 85:    
   print("You scored grade B + ...")    
elif marks > 40 and marks <= 60:  
   print("You scored grade B ...")    
elif (marks > 30 and marks <= 40):    
   print("You scored grade C ...")    
else:    
   print("Sorry you are fail ?")    
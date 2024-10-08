#Generate a multiplication table for any give number by user.
#Hint: 
#Use input()
#For example: if user input is 5 means, generate the 5th multiplication table for the range 1 to 10.


a=int(input("Enter a number to generate a table for: "))
for i in range(1,11):  
    print(f"{a}*{i}={a*i}") 

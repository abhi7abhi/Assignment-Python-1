#find the factorial of any number entered by a user using for loop
#use the logic fact=fact*i in the looping statements
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print("The factorial of the number", num, "is",  fact)
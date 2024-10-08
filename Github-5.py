#what will be the output of the code snippet below:

for index in range(50,30,-3):
    print(index, end=" ")
#it prints the following numbers: 50 47 44 41 38 35 32

a=int(input("Enter a number to generate a table for: "))
for i in range(1,11):       #goes till 10 only
    print(f"{a}*{i}={a*i}")  #prints the table for the given number
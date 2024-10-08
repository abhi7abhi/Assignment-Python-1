#write a program to find whether the given string is a palindrome or not

string=input("Enter a string: ")
if string ==string[::-1]:
    print(f"{string} is a palindrome")
else: 
    print(f"{string} is not a palindrome")
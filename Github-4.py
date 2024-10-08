#write a program to find the median of 3 numbers without using the sort() function

num1=int(input('Enter a number: '))
num2=int(input('Enter a number: '))
num3=int(input('Enter a number: '))
if (num1>=num2 and num1<=num3) or (num1<=num2 and num1>=num3):
    median=num1
elif(num2>=num1 and num2<=num3) or (num1<=num2 and num2>=num3):
    median=num2
else:
    median=num3
print('The median is: ', median)
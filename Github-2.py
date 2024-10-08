#program to count the number of alphabets and number of digits in the string "Mahendran-6066681"
#use looping and conditional statements

string = "Mahendran-6066681"
count_alpha = 0
count_digit = 0

for char in string:
    if  char.isalpha():
        count_alpha += 1
    elif char.isdigit:
        count_digit += 1

print('The number of alphabets in the string "Mahendran-6066681" is: ' ,count_alpha)
print('The number of digits in the string  "Mahendran-6066681" is: ',count_digit)
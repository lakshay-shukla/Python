# Loops --> Repeat one piece of same code/code. like flipkart, amazon
# while loop --> used when you want to repeat a task until a certain condition changes.
# it stops when a condition becomes false

# Example 1. Program to print the table.
number = int(input('Enter a number: '))
i = 1
while i<11:
    print(number,'*',i,'=',number * i)
    i += 1

# Example 2.  Sum of all digits of a given number.
number = int(input('Enter a number: '))
digit_sum = 0
while number > 0:
    last_digit = number % 10
    digit_sum += last_digit
    number = number // 10
print("Sum of Digits",digit_sum)

# method to take input {input('Enter your name: ')}
# #Program to add two no.s

#1. take input from users and store them in a variable
fnum = input('Enter First Number: ')
snum = input('Enter second Number: ')
#2. add the two variable
result = int(fnum) + int(snum)
#3. print the result
print(result)
print(type(fnum))
print(type(snum))
# Information
# Type coversion karte hue fnum and snum me koi change nahi hoga uske andar jo hai wo uske jaisa same bana dega bss data type change karke
# Python Type Conversion does not change the old data its create the new value and we work on it.

# Better method to write this code

# take input from users and store them in a variable
fnum = int(input('enter first number'))
snum = int(input('enter second number'))
#print(type(fnum),type(snum))
# add the 2 variables
result = fnum + snum
# print the result
print(result)
print(type(fnum))
print(type(snum))

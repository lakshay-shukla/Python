# Arithmetic Operators (+, - , *, /)
print(5+6) #Addition
print(6-5) #Subtraction
print(5*6) #Multiplication
print(5/2) #Division
print(5//2) #Interger Division --> its convert decimal answer into integer
print(5%2) #Modular Operator --> it gives remainder as answer
print(5**2) #Power of Operator --> 5 to the power 2

# Relational Operators --> its for comparision
print(4>5)
print(4<5)
print(4>=4)
print(4<=4)
print(4==4)
print(4!=4)

# Logical Operators
#1 and --> When both values are true (1) then its true otherwise false (0)
print(1 and 0)
#2 or --> When both values are false (0) then its false otherwise true (1)
print(1 or 0)
#3 not --> its convert false to true and vice versa
print(not 1)

# Bitwise Operators --> These are special operators which operates on binary values
# convert given no. in binary then solve it
#1 bitwise and
print(2 & 3) # perform 'and' operation on binary no. of given no.'s
#2 bitwise or
print(2 | 3) # perform 'or' operation on binary no. of given no.'s
#3 bitwise xor (or + not)  --> when both are same then its false (0) otherwise true (1)
print(2 ^ 3) # perform 'xor' operation on binary no. of given no.'s
#4 bitwise not --> in binary its change 0 to 1 and 1 to 0
print(~ 3) #  perform 'not' operation on binary no. of given no.'s
#5 Bitwise Right shift
print(4 >> 2)
#6 Bitwise Left shift
print(4 << 2)

# Assignment Operators (=) a = 2
a = 2
a += 2 # a = a + 2
print(a)

# Membership Operators (in / not in)--> its check something is exist or not in particular word or anything
# it works on all data types
print('D' in 'Delhi')
print(1 in [2,3,4,5,6])

# Program - Find the sum of a 3 digit number entered by the user

number = int(input('Enter a 3 digit no. : '))

# 345%10 -> 5
a = number%10  # it takes remainder

number = number//10  # it gives 34

# 34%10 -> 4
b = number % 10

number = number//10
# 3 % 10 -> 3
c = number % 10

print(a + b + c)
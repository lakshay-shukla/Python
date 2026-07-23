# List Comprehension--> It provides a concise/Shortcut way of creating lists.
# Method to create --> new_list = [expression for item in iterable if condition == True]
# Advantages of List Comprehension:
#1. More time-efficient and space-efficient than loops.
#2. Require fewer lines of code.
#3. Transforms iterative statement into a formula.

# example 1. Add 1 to 10 numbers to a list.
# Normal Method
L = []
for i in range(1,11):
  L.append(i)
print(L)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List Comprehension Method
L = [i for i in range(1,11)]  # expression = i , Iterable = (1,11)
print(L)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# example 2. scalar multiplication on a vector
v = [2,3,4]
s = -3
print([s*i for i in v])  #[-6,-9,-12]

# example 3. Add squares
L = [1,2,3,4,5]
print([i**2 for i in L]) # [1, 4, 9, 16, 25]

# example 4. Print all numbers divisible by 5 in the range of 1 to 50
print([i for i in range(1,51) if i%5 == 0])  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


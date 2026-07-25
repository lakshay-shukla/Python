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

# example 5. find languages which start with letter p
languages = ['java','python','php','c','javascript']
print([language for language in languages if language.startswith('p')])

# example 6. Nested if with List Comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']
# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'
print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')])

# example 7. Print a (3,3) matrix using list comprehension -> Nested List comprehension
print([[i*j for i in range(1,4)] for j in range(1,4)])

# example 8. cartesian products -> List comprehension on 2 lists together
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print([i*j for i in L1 for j in L2])
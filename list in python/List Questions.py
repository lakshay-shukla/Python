# Example- 1. How to take list as input from user.
# A. list string input
li = input("enter a list: ").split()
print(li)

# B. list number input
num_li = list(map(int, input("enter a list: ").split()))
print(num_li)

# Example- 2. Write a program to merge 2 list without using the + operator
L1 = [1,2,3,4]
L2 = [5,6,7,8]
L1.extend(L2)
print(L1)

# Example- 3. Create 2 lists from a given list where
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers
L = [1,2,3,4,5,6]
even_list = [ ]
odd_list = [ ]
for i in L:
    if i%2 == 0 :
        even_list.append(i)
    elif i%2 != 0:
        odd_list.append(i)
print(odd_list)
print(even_list)

# Example- 4. Write a program to replace an item with a different item if found in the list.
# replace 3 with 300
L = [1,2,3,4,5,3]
for x in L:
    if x == 3:
        pos = L.index(3)
        L[pos] = 300
print(L)
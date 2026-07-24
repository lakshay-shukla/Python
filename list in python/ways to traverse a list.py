# itemwise
L = [1,2,3,4]
for i in L:
  print(i)  # 1 2 3 4

# indexwise
L = [1,2,3,4]
for i in range(0,len(L)):
  print(L[i])  # 1 2 3 4
  print(i)  # 0 1 2 3  (index value)

# Disadvantages of list
#1. Slow then Array
#2. Risky usage
a = [1,2,3]
b = a
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]
# This program has an error because you change in a only but its point b also so b is also change.
# The correct method is you want to change in 16 line of code "b = a.copy()".

#3. eats up more memory

# Tuple --> A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.
# In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.
#Characterstics
#A. Ordered
#B. Unchangeble
#C. Allows duplicate

#1. Creating Tuples
# Empty
t1 = ()
print(t1)  # ()
# Create a tuple with a single item
t2 = ('hello',)
print(t2)  # ('hello',)
print(type(t2))  # <class 'tuple'>
# Homogenous
t3 = (1,2,3,4)
print(t3)  # (1, 2, 3, 4)
# Hetrogenous
t4 = (1,2.5,True,[1,2,3])
print(t4)  # (1, 2.5, True, [1, 2, 3])
# Tuple
t5 = (1,2,3,(4,5))
print(t5)   #  (1, 2, 3, (4, 5))
# Using type conversion
t6 = tuple('hello')
print(t6)  # ('h', 'e', 'l', 'l', 'o')

#2. Accessing Items
# Indexing
t3 = (1,2,3,4)
print(t3[0])
print(t3[-1])
# Slicing
t5 = (1,2,3,(4,5))
print(t5[-1][0])
t = (1,2,3,4,5)
print(t[-1:-4:-1])

#3. Editing items --> Not possible because of immutable nature of tuble just like strings.

#4. Adding items --> Not possible because of immutable nature of tuble just like strings.

#5. Deleting items
t3 = (1,2,3,4)
print(t3)
del t3
print(t3)

#6. Operations on Tuples
# + and *
t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1 + t2)
print(t1*3)
# membership
print(1 in t1)
# iteration
for i in t1:
  print(i)
# Sets --> A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# However, a set itself is mutable. We can add or remove items from it.
# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.
# Characterstics:
#1. Unordered
#2. Mutable
#3. No Duplicates
#4. Can't contain mutable data types

s1 = {1,2,3}
s2 = {3,2,1}
print(s1 == s2)

#1. Creating Sets
# empty
s = set()
print(s)
print(type(s))
# 1D and 2D
s1 = {1,2,3}
print(s1)
# s2 = {1,2,3,{4,5}}
# print(s2)   # it gives error because sets Can't contain mutable data types
# homo and hetro
s3 = {1,'hello',4.5,(1,2,3)}
print(s3)
# using type conversion
s4 = set([1,2,3])
print(s4)
# duplicates not allowed
s5 = {1,1,2,2,3,3}
print(s5)
# set can't have mutable items
# s6 = {1,2,[3,4]}
# print(s6)  # it gives error because sets Can't contain mutable data types

#2. Accessing Items --> You can't indexing and slicing because of unordered nature of sets

#3. Editing Items --> Editing is not allowed in sets

#4. Adding Items
S = {1,2,3,4}
# add
S.add(5)
print(S)
# update
S.update([5,6,7])
print(S)

#5. Deleting Items
# del
s = {1,2,3,4,5}
# print(s)
# del s[0]
# print(s)
# discard
# s.discard(50)
# print(s)
# remove
# s.remove(50)
# print(s)
# pop
# s.pop()
# clear
s.clear()
print(s)


# Set Operations

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
#1. Union(|)
print(s1 | s2)
#2. Intersection(&)
print(s1 & s2)
#3. Difference(-)
print(s1 - s2)
print(s2 - s1)
#4. Symmetric Difference(^)
print(s1 ^ s2)
#5. Membership Test
print(1 not in s1)
#6. Iteration
for i in s1:
  print(i)
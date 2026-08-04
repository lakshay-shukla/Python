# Sets Function

#1. len/sum/min/max/sorted
s = {3,1,4,5,2,7}
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s,reverse=True))
#2. union/update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
# s1 | s2
s1.union(s1)
s1.update(s2)
print(s1)
print(s2)
#3. intersection/intersection_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.intersection(s2)
s1.intersection_update(s2)
print(s1)
print(s2)
#4. difference/difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.difference(s2)
s1.difference_update(s2)
print(s1)
print(s2)
#5. symmetric_difference/symmetric_difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.symmetric_difference(s2)
s1.symmetric_difference_update(s2)
print(s1)
print(s2)
#6. isdisjoint/issubset/issuperset
s1 = {1,2,3,4}
s2 = {7,8,5,6}
print(s1.isdisjoint(s2))
s1 = {1,2,3,4,5}
s2 = {3,4,5}
print(s1.issuperset(s2))
#7. copy
s1 = {1,2,3}
s2 = s1.copy()
print(s1)
print(s2)


# Frozen Set --> Frozen set is just an immutable version of a Python set object.

# create frozenset
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])
print(fs1 | fs2)

# what works and what does not
# works -> all read functions
# does't work -> write operations

# When to use
# 2D sets
fs = frozenset([1,2,frozenset([3,4])])
print(fs)


# Set Comprehension
# examples
print({i**2 for i in range(1,11) if i>5})  # {64, 36, 100, 49, 81}


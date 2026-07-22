#1. What are Lists--> Lists are used to store multiple items in a single variable.
#2. List vs Array
# Array: Homogeneous; Contiguous memory; Fast; Numerical/Scientific use.
# List: Heterogeneous; Non-contiguous memory; Programmer-friendly; General-purpose.

#3. Arrays vs. Lists in Memory:
# Arrays:
#A. int arr[50]; ---> 50 contiguous memory blocks.
#B. Elements stored in binary form at consecutive addresses.
# Lists:
#A. list_example = [1, 2, 3] ---> Elements at different locations.
#B. Stores references/pointers to elements, not the values.

L = [1,2,3]
print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))
print(id(1))
print(id(2))
print(id(3))

# Characterstics of a List:
#1. Ordered
#2.Mutable
#3. Heterogeneous
#4. Duplicates allowed
#5. Dynamic size
#6. Nesting supported
#7. Indexable
#8. Any object type

L = [1,2,3,1]
L1 = [3,2,1]
print(L == L1)  #False

#1. Creating a list:
# Empty
print([])
# 1D -> Homo
print([1,2,3,4,5])
# 2D
print([1,2,3,[4,5]])
# 3D
print([[[1,2],[3,4]],[[5,6],[7,8]]])
# Hetrogenous
print([1,True,5.6,5+6j,'Hello'])
# Using Type conversion
print(list('hello'))

#2. Accessing Items from a List:
# Indexing
L = [[[1,2],[3,4]],[[5,6],[7,8]]]
#positive
print(L[0][0][1])
# Slicing
L = [1,2,3,4,5,6]
print(L[::-1])

#3. Adding Items to a List:
# append
L = [1,2,3,4,5]
L.append(True)
print(L)
L = [1,2,3,4,5]
L.append([6,7,8])
print(L)
# extend
L = [1,2,3,4,5]
L.extend([6,7,8])
print(L)
L = [1,2,3,4,5]
L.extend('delhi')
print(L)
# insert
L = [1,2,3,4,5]
L.insert(1,100)
print(L)

#4. Editing items in a List:
L = [1,2,3,4,5]
# editing with indexing
L[-1] = 500
# editing with slicing
L[1:4] = [200,300,400]
print(L)

#5. Deleting items from a List:
#A. delete
L = [1,2,3,4,5]
# indexing
del L[-1]
# slicing
del L[1:3]
#B. remove
L = [1,2,3,4,5]
L.remove(5)
print(L)
#C. pop
L = [1,2,3,4,5]
L.pop()
print(L)
#D. clear
L = [1,2,3,4,5]
L.clear()
print(L)






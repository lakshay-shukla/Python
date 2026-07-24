# Zip Function --> The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

# Write a program to add items of 2 lists indexwise
L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]
list(zip(L1,L2))
print([i+j for i,j in zip(L1,L2)])  # [0, 0, 0, 0]

# List can store any kind of object in it.
L = [1,2,print,type,input]
print(L) # [1, 2, <built-in function print>, <class 'type'>, <bound method Kernel.raw_input of <google.colab._kernel.Kernel object at 0x7f7a67452a90>>]
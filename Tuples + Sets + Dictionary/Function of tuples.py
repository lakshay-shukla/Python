# Tuple Functions
#1. len/sum/min/max/sorted
t = (1,2,3,4)
print(len(t))
print(sum(t))
print(min(t))
print(max(t))
print(sorted(t,reverse=True))

#2. count
t = (1,2,3,4,5)
print(t.count(50))

#3. index
print(t.index(3))

# Difference between Lists and Tuples
#1. Syntax
#2. Mutability
#3. Speed
import time
L = list(range(100000000))
T = tuple(range(100000000))
start = time.time()
for i in L:
  i*5
print('List time',time.time()-start)  # List time 9.853569507598877
start = time.time()
for i in T:
  i*5
print('Tuple time',time.time()-start)  # Tuple time 8.347511053085327
#4. Memory
import sys
L = list(range(1000))
T = tuple(range(1000))
print('List size',sys.getsizeof(L))  # List size 9120
print('Tuple size',sys.getsizeof(T))  # Tuple size 8056
#5. Built in functionality
#6. Error prone
#7. Usability

# Special Syntax
#1. tuple unpacking
a,b,c = (1,2,3)
print(a,b,c)  # 1 2 3

a,b = (1,2,3)
print(a,b)  # this gives error because the no. of item in tuble is more then values.

a = 1
b = 2
a,b = b,a
print(a,b)  # 2 1

a,b,*others = (1,2,3,4)
print(a,b)  # 1 2
print(others)  # [3, 4]

# zipping tuples
a = (1,2,3,4)
b = (5,6,7,8)
print(tuple(zip(a,b)))  # ((1, 5), (2, 6), (3, 7), (4, 8))


#1. len/min/max/sorted
L = [2,1,5,7,0]
print(len(L))  # 5
print(min(L))  # 0
print(max(L))  # 7
print(sorted(L,reverse=True))  # [7, 5, 2, 1, 0]

#2. count
L = [1,2,1,3,4,1,5]
print(L.count(5))  # 1

#3. index
L = [1,2,1,3,4,1,5]
print(L.index(1))  # 0

#4. reverse
L = [2,1,5,7,0]
# permanently reverses the list
L.reverse()
print(L)  # [0, 7, 5, 1, 2]

#5. sort (vs sorted)
L = [2,1,5,7,0]
print(L)  # [2, 1, 5, 7, 0]
print(sorted(L))  # [0, 1, 2, 5, 7]
print(L)  # [2, 1, 5, 7, 0]
L.sort()
print(L)  # [0, 1, 2, 5, 7]

#6. copy -> shallow
L = [2,1,5,7,0]
print(L)  # [2, 1, 5, 7, 0]
print(id(L))  # 2283412502336
L1 = L.copy()
print(L1)  # [2, 1, 5, 7, 0]
print(id(L1))  # 2283412385984
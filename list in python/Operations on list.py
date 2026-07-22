# Operations on Lists:
#1. Arithmetic:
# Arithmetic (+ ,*)
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print(L1 + L2)
print(L1*3)

#2. Membership:
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
print(5 not in L1)
print([5,6] in L2)

#3. Loop:
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]
L3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
for i in L3:
  print(i)
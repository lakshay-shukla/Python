#1.
#*
#* *
#* * *
#* * * *
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end=" ")
    print()


#2.
#1
#1 2
#1 2 3
#1 2 3 4
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#3.
#1
#1 2 1
#1 2 3 2 1
#1 2 3 4 3 2 1
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    for k in range(i - 1, 0, -1):
        print(k, end=" ")
    print()


#4.
#1 1 1 1
#2 2 2 2
#3 3 3 3
#4 4 4 4
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        print(i, end=" ")
    print()


#5.
#1 2 3 4
#1 2 3
#1 2
#1
rows = int(input("Enter number of rows: "))
for i in range(rows,0,-1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#6.
#A
#A B
#A B C
#A B C D
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(chr(j+64), end=" ")
    print()


#7.
#1
#A B
#1 2 3
#A B C D
#1 2 3 4 5
rows = int(input("Enter number of rows: "))
for i in range(1, rows):
    for j in range(1, i + 1):
        if i%2 == 0:
            print(chr(j+64), end=" ")
        else:
            print(j, end=" ")
    print()


#8.
#*
#* *
#* * *
#* * * *
#* * *
#* *
#*
rows = int(input("Enter number of rows: "))
for i in range(1, rows):
    for j in range(1, i + 1):
        print('*', end=" ")
    print()
for k in range(3,0,-1):
    for p in range(1, k + 1):
        print('*', end=" ")
    print()


#9.
#* * * * * *
#* *
#* *
#* * * * * *
for i in range(1, 5):
    for j in range(1, 7):
        if i == 1:
            print('*', end=" ")
        elif i == 4:
            print('*', end=" ")
    for k in range(1,3):
        if i == 2:
            print('*', end=" ")
        elif i == 3:
            print('*', end=" ")
    print()


#10.
#* * * *
#* * * *
#* * * *
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end=" ")
    print()


#11.
#A
#A B
#A B C
#A B C D
for i in range(1, 5):
    for j in range(1, i + 1):
        print(chr(j+64), end=" ")
    print()


#12.
#1
#2 1
#3 2 1
#4 3 2 1
for i in range(1, 5):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()


#13.
# * * * * * * *
# * * *   * * *
# * *       * *
# *           *
# * *       * *
# * * *   * * *
# * * * * * * *
for i in range(1,8):
    for j in range(1,8):
        if j<= 5-i or j>= 3+i:
            print('*',end=' ')
        elif j<= i-3 or j>= 11-i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


#14.
# *           *
#   *       *
#     *   *
#       *
for i in range(1,5):
    for j in range(1,8):
        if j==i or j== 8-i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


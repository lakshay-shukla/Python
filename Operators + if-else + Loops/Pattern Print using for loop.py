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


# Nested Loop- A nested loop in Python is a loop placed inside another loop.

# Example - # Examples -> unique pairs
for i in range(1,6):
  for j in range(1,6):
    print(i,j)


# Example on Patterns
#1.
# *
# * *
# * * *
# * * * *
# * * * * *

rows = int(input('enter number of rows: '))
for i in range(1,rows+1):
  for j in range(1,i+1):
    print('*',end=' ')
  print()

#2.
#1
#121
#12321
#1234321

rows = int(input('enter number of rows: '))
for i in range(1,rows+1):
  for j in range(1,i+1):
    print(j,end='')
  for k in range(i-1,0,-1):
    print(k,end='')

  print()

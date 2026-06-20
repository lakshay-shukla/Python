# We use if-else for branching in python when you have one or more option/possibilities and you want to select one only.
# Indentation --> It is the one tab space.
# For two possibilities 'if-else' is sufficient but if you have two or more possibilities you use 'elif'.
# Nested if-else --> You can also use 'if-else' in 'if' or 'elif' block

# Program for login
# login program and indentation
# email -> lakshayshukla123@gmail.com
# password -> 1234

email = input('enter email: ')
password = input('enter password: ')

if email == 'lakshayshukla123@gmail.com' and password == '1234':
  print('Welcome')
elif email == 'lakshayshukla123@gmail.com' and password != '1234':
  # tell the user
  print('Incorrect password')
  password = input('enter password again')
  if password == '1234':
    print('Welcome,finally!')
  else:
    print('beta tumse na ho paayega!')
else:
  print('Not correct')

  # if-else examples
  # 1. Find the min of 3 given numbers
  a = int(input('enter number 1: '))
  b = int(input('enter number 2: '))
  c = int(input('enter number 3: '))

  if a<b and a<c:
    print('smallest is:', a)
  elif b<c:
    print('smallest is:', b)
  else:
    print('smallest is:', c)





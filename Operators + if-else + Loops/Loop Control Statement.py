# Break --> This is used to break a loop. example 'Linear Search'

# example 1.
for i in range(1,10):
  if i == 5:
    break
  print(i)

# example 2. Prime No.
lower = int(input('enter lower range: '))
upper = int(input('enter upper range: '))

for i in range(lower,upper+1):
  for j in range(2,i):
    if i%j == 0:
      break
  else:
    print(i)


# Continue --> This is used to skip the iteration in loop.
for i in range(1,10):
  if i == 5:
    continue
  print(i)


# Pass --> This is used to pass the complete loop without any error
for i in range(1,10):
  pass
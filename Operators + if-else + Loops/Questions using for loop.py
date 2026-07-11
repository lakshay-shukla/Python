# 1. write a program to find a factorial of a number.
num = int(input("Enter a number: "))
fact = 1
for i in range(1,num+1):
  fact = fact * i
print('Factorial is:', fact)

#2. Program to calculate power.
N1 = int(input('Enter number N1: '))
N2 = int(input('Enter number N2: '))
power = 1
for i in range(1,N2+1):
  power = N1*power
print(power)

#3. Print All Armstrong no. between 1 to 500.
for num in range (1,500):
  if num < 10:
    power = 1
  elif num < 100:
    power = 2
  else:
    power = 3
  temp = num
  total_sum = 0
  for i in range(power):
    digit = temp % 10
    total_sum = total_sum + (digit ** power)
    temp = temp // 10
  if total_sum == num:
    print(num)

# 4. Print all prime no. between 1 to 300.
for i in range(2,300):
  for j in range(2,i):
    if i%j==0:
      break
  else:
    print(i)

# 5. Generate all combinations of 1,2 and 3
for i in range(1,4):
  for j in range(1,4):
    for k in range(1,4):
      print(str(i)+ str(j) + str(k))
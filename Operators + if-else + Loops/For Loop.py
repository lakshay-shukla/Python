# For loop--> A for loop in Python is used to iterate over a sequence (list, tuple, string, dictionary, set, or range)
# example 1
for i in {1,2,3,4,5}:
  print(i)

# Range in for loop --> The range() function generates a sequence of numbers, which can be used to iterate over with a for loop.
# 1st no. is included in range but 2nd is excluded and 3rd no. in range is step size

# example 2
for i in range(1,6):
    print(i)

# For loop with else
for i in range(1,6):
    print(i)
else:
    print("Loop finished")


# Example Question-1  The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years.

curr_pop = 10000
for i in range(10,0,-1):
  print(i,curr_pop)
  curr_pop /= 1.1

# Example -2:  1/1! + 2/2! + 3/3! + ...

n = int(input("Enter a n: "))
num = 0
fact = 1

for i in range(1,n+1):
  fact = fact*i
  num = num + i/fact
print(num)


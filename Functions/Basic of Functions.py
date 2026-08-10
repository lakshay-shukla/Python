#1. Function --> functions are reusable blocks of code that perform a specific task. They help make programs modular, readable, and maintainable.
#2. DocStrings --> A docstring is a string literal placed immediately after a function definition to describe its purpose, parameters, return values, and other relevant details.
# It serves as built-in documentation accessible at runtime via .__doc__ or help().

# Create a function(with docstring)
def is_even(num):
  """
  This function returns if a given number is odd or even
  input - any valid integer
  output - odd/even
  created on - 16th Nov 2022
  """
  if type(num) == int:
    if num % 2 == 0:
      return 'even'
    else:
      return 'odd'
  else:
    return 'pagal hai kya?'

# function Calls
for i in range(1,11):
  x = is_even(i)
  print(x)

# To print Docstring from function (.__doc__)
print(is_even.__doc__)

#3. Parameters --> Input values when create a function.
#4. Arguments --> Input values when calls a function.

#4. Types of Arguments
#A. Default Argument --> We give default values for a and b
def power(a=1,b=1):
  return a**b
print(power())

#B. Positional Argument --> it's define values automatic according to its position values
print(power(2,3))

#C. Keyword Argument --> We set the values for a and b randomly
print(power(b=3,a=2))


# *args and **kwargs --> *args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function.
# Both used for gives multiple arguments

#1. *args --> Allows us to pass a variable number of non-keyword arguments to a function.
# it show's input in tuples form
def multiply(*args):
  product = 1
  for i in args:
    product = product * i
  print(args)
  return product
print(multiply(1,2,3,4,5,6,7,8,9,10,12)) # Function Call

#2. **kwargs --> **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.
# it show's input in Dictionary form.
def display(**kwargs):
  for (key,value) in kwargs.items():
      print(key,'->',value)
print(display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad'))

# Points to remember while using *args and **kwargs
#1. order of the arguments matter(normal -> *args -> **kwargs)
#2. The words “args” and “kwargs” are only a convention, you can use any name of your choice
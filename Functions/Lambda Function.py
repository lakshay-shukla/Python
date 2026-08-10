# Lambda Function --> A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Create lambda Expression --> lambda a,b: a+b
#1. lambda keyword --> Creates the lambda expression
#2. a,b parameters --> One or more parameters are supported. Parameters must be seperated by a comma (,) and no parentheses.
#3. Colon (:) --> This is a cue for the expression
#4. a+b (expression) --> Must be a single valid Python Expression

# Find Power x -> x^2
A = lambda x:x**2
print(A(5))

# Additon  x,y -> x+y
a = lambda x,y:x+y
print(a(5,2))

# check if a string has 'a'
a = lambda s:'a' in s
print(a('hello'))

# odd or even
a = lambda x:'even' if x%2 == 0 else 'odd'
print(a(6))

# Diff between lambda vs Normal Function
#1. No name
#2. lambda has no return value(infact,returns a function)
#3. lambda is written in 1 line
#4. not reusable

# why use lambda functions --> They are used with HOF (Higher Order Function).

# Normal Example
def square(x):
  return x**2
def cube(x):
  return x**3

# HOF Example
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))
  print(output)
L = [1,2,3,4,5]
transform(lambda x:x**3,L)
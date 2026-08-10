# The life of function in memory is between Call and Return.
# Function acts like independent program

#1. Variable Scope --> There are Two types of variable scope. (Global and Local)
# Global --> Variable in main program is called global variable.
# Local --> Variables in function program is called local variable.
# Global Variable is used by local variable but local is not used by global.

def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)  # O/P-: 5 6 5

def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)  #O/P-: 2 5

def h(y):
    x += 1
x = 5
h(x)
print(x)  # it gives error local variable is not used by global

def f(x):
   x = x + 1
   print('in f(x): x =', x)  # 4
   return x
x = 3
z = f(x)
print('in main program scope: z =', z)  # 4
print('in main program scope: x =', x)  # 3


#2. Nested Functions --> Function inside function
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)  # 4
    h()
    return x
x = 3
z = g(x)

def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)  # 4
    x = x + 1
    print('in g(x): x = ', x)  # 5
    h(x)
    return x
x = 3
z = g(x)
print('in main program scope: x = ', x)   # 3
print('in main program scope: z = ', z)   # 4


# Functions are 1st class citizens

#1. type and id
def square(num):
  return num**2
print(type(square))   # <class 'function'>
print(id(square))   # 1658412545504

#2. reassign
x = square
print(id(x))   # 1658412545504
print(x(3))  # 9

#3. deleting a function
del square
square(5)  # NameError: name 'square' is not defined

#4. returning a function
def f():
    def x(a, b):
        return a + b
    return x
val = f()(3, 4)
print(val)

# Benefits of using a Function
#1. Code Modularity
#2. Code Readibility
#3. Code Reusability


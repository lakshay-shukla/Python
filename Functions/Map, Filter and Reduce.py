# Map-:
#1. odd/even labelling of list items
L = [1,2,3,4,5]
S = list(map(lambda x:'even' if x%2 == 0 else 'odd',L))
print(S)  # ['odd', 'even', 'odd', 'even', 'odd']

#2. square the items of a list
R = list(map(lambda x:x**2,[1,2,3,4,5]))
print(R)  # [1, 4, 9, 16, 25]

#3. fetch names from a list of dict
users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]
T = list(map(lambda users:users['gender'],users))
print(T)  # ['male', 'male', 'female']


# Filter-:
#1. numbers greater than 5
L = [3,4,5,6,7]
B = list(filter(lambda x:x>5,L))
print(B)  # [6, 7]

#2. fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']
C = list(filter(lambda x:x.startswith('a'),fruits))
print(C)  # ['apple']


# Reduce-: You can import reduce ( import functools )
#1. sum of all item
import functools
E = functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
print(E)  # 15

#2. find min
D = functools.reduce(lambda x,y:x if x<y else y,[23,11,45,10,1])
print(D)  # 1

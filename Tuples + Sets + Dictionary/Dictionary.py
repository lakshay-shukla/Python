# Dictionary --> Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.
# In some languages it is known as map or assosiative arrays.
# dict = { 'name' : 'Lakshay' , 'age' : 22 , 'gender' : 'male' }
# Characterstics:
#1. Mutable
#2. Indexing has no meaning
#3. keys can't be duplicated
#4. keys can't be mutable items

#1. Creating Dictionary
# empty dictionary
d = {}
print(d)
# 1D dictionary
d1 = { 'name' : 'Lakshay' ,'gender' : 'male' }
print(d1)
# with mixed keys
d2 = {(1,2,3):1,'hello':'world'}
print(d2)
# 2D dictionary -> example-: JSON
s = {
    'name':'Lakshay',
     'college':'bit',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}
print(s)
# using sequence and dict function
d4 = dict([('name','Lakshay'),('age',22),(3,3)])
print(d4)
# duplicate keys
d5 = {'name':'Lakshay','name':'rashi'}
print(d5)
# mutable items as keys
d6 = {'name':'Lakshay',(1,2,3):2}
print(d6)

#2. Accessing Items
s = {
    'name':'Lakshay',
     'college':'bit',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}
my_dict = {'name': 'Jack', 'age': 26}
# []
print(my_dict['age'])
# get
print(my_dict.get('age'))
print(s['subjects']['maths'])

#3. Adding key value pair
d4['gender'] = 'male'
print(d4)
d4['weight'] = 72
print(d4)
s['subjects']['ds'] = 75
print(s)

#4. Remove key value pair
d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}
# pop
#d.pop(3)
#print(d)
# popitem
#d.popitem()
# d.popitem()
# print(d)
# del
#del d['name']
#print(d)
# clear
d.clear()
print(d)

del s['subjects']['maths']
s

#5. Editing key value pair
s['subjects']['dsa'] = 80
print(s)

# Dictionary Operation
#1. Membership
print(s)
print('name' in s)
#2. Iteration
d = {'name':'nitish','gender':'male','age':33}
for i in d:
  print(i,d[i])
# Dictionary Functions
d = {'name': 'nitish', 'gender': 'male', 'age': 33}
# len/sorted
print(len(d))
print(d)
print(sorted(d,reverse=True))
print(max(d))
# items/keys/values
print(d.items())
print(d.keys())
print(d.values())
# update
d1 = {1:2,3:4,4:5}
d2 = {4:7,6:8}
d1.update(d2)
print(d1)

# Dictionary Comprehension --> { key: value 'for' vars 'in' iterable}
#1. print 1st 10 numbers and their squares
print({i:i**2 for i in range(1,11)})

distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print(distances.items())

#2. using existing dict
distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}
print({key:value*0.62 for (key,value) in distances.items()})

#3. using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]
print({i:j for (i,j) in zip(days,temp_C)})

#4. using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}
print({key:value for (key,value) in products.items() if value>0})

#5. Nested Comprehension
# print tables of number from 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})
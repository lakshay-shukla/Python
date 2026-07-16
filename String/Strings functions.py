#1. Common Functions
# len()
c = 'kolkata'
print(len(c))
# max()
print(max(c))
# min()
print(min(c))
# sorted()
print(sorted(c))
print(sorted(c, reverse=True))

#2. Count function
print("it is raining".count("i"))
print("it is raining".count("ing"))
print("it is raining".count("x"))

#3. Find/Index
print("it is raining".find("i"))
print("it is raining".find("g"))
print("it is raining".find("raining"))
print("it is raining".find("x"))
print("it is raining".index("raining"))
print("it is raining".index("x")) # this gives error because x is not present in the sentence.

#4. Capitalize / Title / Upper / Lower / Swapcase
c = "hello world"
print(c.capitalize())
print('it is raining today'.capitalize())
print('it is raining today'.title())
print(c.upper())
print(c.lower())
print("KoLkAtA".swapcase())

#5. endswith/startswith
print("it is raining".endswith("ing"))
print("it is raining".endswith("ingf"))
print("it is raining".startswith("it"))

#6. format
print("Hello my name is {} and I am {}".format("Saurabh", 22))
print("Hello my name is {1} and I am {0}".format("Saurabh", 22))
print("Hello my name is {age} and I am {name}".format(name = "Saurabh", age = 22))
print("Hello my name is {name} and I am {name}".format(name = "Saurabh", age = 22, weight = 90))

#7. isalnum/isalpha/isdecimal/isdigit/isidentifier
print("FLAT20".isalnum()) # Alphanumeric
print("FLAT20&".isalnum())
print("FLAT".isalpha()) # Alphabetic
print("FLAT20".isalpha())
print("20".isdigit())
print("20A".isdigit())
print("Hello World".isidentifier())
print("Hello_World".isidentifier())

#8. Split
print("who is the pm of india".split())
print("who is the pm of india".split("pm"))
print("who is the pm of india".split("i"))
print("who is the pm of india".split("x"))

#9. Join
print(" ".join(['who', 'is', 'the', 'pm', 'of', 'india']))
print("-".join(['who', 'is', 'the', 'pm', 'of', 'india']))

#10. Replace
print("Hi my name is Saurabh".replace("Saurabh", "Siddhant"))

#11. Strip
print('nitish                           '.strip())

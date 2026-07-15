#1. Arithmetic: Concatenation (+), Repetition (*)
print("Hello" + "-" + "World")
print("*"*50)
print("Hello"*4)

#2. Relational: Equality (==), Inequality (!=), Comparison (<, >, <=, >=)
print("Hello" == "World")
print("Hello" != "World")
print("Mumbai" > "Pune") # Lexiographically
print("Goa" > "Kolkata")
print("kol" < "Kol")

#3. Logical: and, or, not
# ""        ---> False
# "saurabh" ---> True
print("Hello" and "World")
print("" and "Hello")
print("" or "World")
print("Hello" or "World")
print("Hello" and "World")
print(not "Hello")
print(not "Hello")
print(not "")

#4. Loops: for loop, while loop
c = "Hello World"
for i in c:
    print(i)

for i in c[2:7]:
    print(i)

for i in c[2:7:2]:
    print(i)

for i in c[::-1]:
    print(i)

#5. Membership: in, not in
c = "Hello World"
print(c)
print('H' in c)
print('h' in c)
print('World' not in c)

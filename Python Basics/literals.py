# Literals (the value is stored in variable is known as literals (raw value stored in literals)
# varable is a container but the value is stored in variable is known as literals

a = 0b1010 #Binary Literals ('0b' ke aage ka no. bata raha hai ki wo binary me hai)
b = 100 #Decimal Literal
c = 0o310 #Octal Literal ('0o' ke aage ka no. bata raha hai ki wo octal me hai)
d = 0x12c #Hexadecimal Literal ('0x' ke aage ka no. bata raha hai ki wo hexadecimal me hai)
print(a, b, c, d)

#Float Literal
float_1 = 10.5
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3
print(float_1, float_2,float_3)

#Complex Literal
x = 3.14j
print(x, x.imag, x.real)

#Boolean Literals
a = True + 4 # (Python consider true as a 1)
b = False + 10 # (Python consider false as a 0)

print("a:", a) # output 5
print("b:", b) #output 10



# Representation of String
string = 'This is Python'
print(string)

strings = "This is Python"
print(strings)

char = "C"
print(char)

multiline_str = """This is a multiline string with more than one line code."""
print(multiline_str)

# unicode --> Representation of smilies, emojis etc.
unicode = u"\U0001f600\U0001F606\U0001F923"
print(unicode)

# raw string --> like (\n, \t etc)
raw_str = r"raw \n string"
print(raw_str)




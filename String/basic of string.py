# Strings --> Strings are sequence of Characters
#Python String --> In Python specifically, strings are a sequence of Unicode Characters

#1. Creating Strings
s = 'hello'
s = "hello"
# multiline strings
s = '''hello'''
s = """hello"""
s = str('hello')
print(s)
# "it's raining outside" (This is right method)
# 'it's raining outside' (This is wrong method)


#2. Accessing Substrings from a String

#A. Positive Indexing
s = 'hello world'
print(s[1])

#B. Negative Indexing
s = 'hello world'
print(s[-3])

#C. Slicing
s = 'hello world'
print(s[6:0:-2])

#D. Reverse string
print(s[::-1])
s = 'hello world'
print(s[-1:-6:-1])


#3. Editing Strings and Deleting Strings
# Strings are immutable so we can't edit and delete in the string and the string.
s = 'hello world'
s[0] = 'H'

s = 'hello world'
del s
print(s)

s = 'hello world'
del s[-1:-5:2]
print(s)
# This editing and deleting column gives error because string is immutable.
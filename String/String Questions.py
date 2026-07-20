#1. Find the length of a given string without using the len() function
s = input('enter the string: ')
counter = 0
for i in s:
  counter += 1
print('length of string is',counter)

#2. # Extract username from a given email.
# Eg if the email is lakshayshukla123@gmail.com
# then the username should be lakshayshukla123
e_mail = input('Enter your e-mail address: ')
position = e_mail.index('@')
print(e_mail[0:position])

#3. # Count the frequency of a particular character in a provided string.
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.
string = input('enter the string: ')
character = input('enter the character: ')
print('Frequency is: ',string.count(character))

#4. Write a program which can remove a particular character from a string.
s = input('enter the string: ')
term = input('what would like to remove: ')
result = ''
for i in s:
  if i != term:
    result = result + i
print(result)

#5. Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam
s = input('enter the string: ')
flag = True
for i in range(0,len(s)//2):
  if s[i] != s[len(s) - i -1]:
    flag = False
    print('Not a Palindrome')
    break
if flag:
  print('Palindrome')

#6. Write a program to count the number of words in a string without split()
s = input('enter the string: ')
L = []
temp = ''
for i in s:
  if i != ' ':
    temp = temp + i
  else:
    L.append(temp)
    temp = ''
L.append(temp)
print(L)

#7. Write a python program to convert a string to title case without using the title()
s = input('enter the string: ')
L = []
for i in s.split():
  L.append(i[0].upper() + i[1:].lower())
print(" ".join(L))

#8. Write a program that can convert an integer to string.
number = int(input('enter the number: '))
digits = '0123456789'
result = ''
while number != 0:
  result = digits[number % 10] + result
  number = number//10
print(result)
print(type(result))

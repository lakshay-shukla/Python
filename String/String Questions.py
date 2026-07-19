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
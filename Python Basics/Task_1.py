#Q-1 Print the given strings as per stated format.
# Given strings**: "Data" "Science" "Mentorship" "Program" "By" "CampusX"
# Output-: Data-Science-Mentorship-Program-Started-By-CampusX
print("Data","Science","Mentorship","Program","Started", "By","CampusX", sep= '-')

#Q-2  Write a program that will convert Celsius value to Fahrenheit.
A = int(input('Enter a celsius temperature: '))
B =  (A *1.8) + 32
print(B)

#Q-3  Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.
A = int(input('Enter a number 1st: '))
B = int(input('Enter a number 2nd: '))
A,b = B,A
print(A,b)

#Q-4 Write a program to find the Euclidean distance between two coordinates.Take both the coordinates from the user as input.
X1 = int(input('Enter a coordinate x1: '))
X2 = int(input('Enter a coordinate x2: '))
Y1 = int(input('Enter a coordinate y1: '))
Y2 = int(input('Enter a coordinate y2: '))
A = ((Y1-X1)**2 + (Y2-X2)**2)**0.5
print(A)

#Q-5 Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
P = int(input('Enter the value of Principle: '))
R = int(input('Enter the value of RI: '))
T = int(input('Enter the value of TP: '))
SI = (P*R*T)/100
print(SI)

#Q-6 Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
# For example: Input: heads -> 4 legs -> 12
# Output: dogs -> 2 chicken -> 2
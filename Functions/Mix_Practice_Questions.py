# Q1: List Filtering
# Given a list of salaries: salaries = [25000, 45000, 15000, 60000, 30000]
# Create a new list containing only the salaries that are strictly greater than 35000.
salaries = [25000, 45000, 15000, 60000, 30000]
new_salary = [ ]
for i in salaries:
    if i > 35000:
        new_salary.append(i)
print(new_salary)

# Q2: Dictionary Manipulation
# Given a dictionary: user = {"name": "Aman", "age": 24, "city": "Delhi"}
# Add a new key-value pair {"is_active": True} and update the value of "city" to "Bangalore".
user = {"name": "Aman", "age": 24, "city": "Delhi"}
user["city"] = "bangalore"
user["is_active"] = True
print(user)

# Q3: Loops and Conditional Logic (Missing Data Handling)
# Given a list of data points: data = [10, 25, -1, 40, -1, 55]
# Iterate through the list using a for loop. If the value is -1, print "Missing Data".
# Otherwise, print "Valid Data: [value]".
data = [10, 25, -1, 40, -1, 55]
for i in data:
    if i == -1:
        print('Missing Data')
    else:
        print('Valid Data: ', [i])

# Q4: Custom Functions
# Create a function named 'apply_discount(price, discount_percent)'.
# The function should calculate and return the final discounted price.
def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

print(apply_discount(1000, 10))

# Q5: Lambda and Map Functions
# Write a lambda function that returns the square of a number.
# Use the map() function to apply this lambda function to the list nums = [2, 4, 6, 8]
# and print the resulting new list.
A = lambda x: x ** 2
num = [2, 4, 6, 8]
print(A(5))
R = list(map(lambda x: x ** 2, num))
print(R)
# Example 1 - if else condition
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Example 2 - if else condition
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Example 3 - if else condition
# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

# 3.1.1.10 LAB - Solution

flower = str(input("Please enter a flower name: "))

if flower == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif flower == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not {}!".format(flower))

# 3.1.1.11 LAB - Tax Calculator

income = float(input("Enter the annual income: "))

if income < 85528:
    tax = (income * 0.18)-556.02
else:
    surplus = (income-85528)*0.32
    tax = surplus + 14839.02

if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# 3.1.1.12 LAB - Leap/Common year
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")
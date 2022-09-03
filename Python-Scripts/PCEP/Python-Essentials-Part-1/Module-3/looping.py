# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# Using a counter variable to exit a loop
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# 3.2.1.3 LAB - Guess Number
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

result = False

while result is False:
    num = int(input("Please enter a numer: "))
    if num == 777:
        print("Well done, muggle! You are free now.")
        result = True
    else:
        print("Ha ha! You're stuck in my loop!")

# For and range function.
for i in range(2, 1):
    print("The value of i is currently", i)

# Print first powers of 2
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2
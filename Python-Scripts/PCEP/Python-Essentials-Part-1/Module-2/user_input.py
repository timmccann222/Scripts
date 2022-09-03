# The input() function is able to read data entered by the user and to return the same data to the running program.
# The result of the input() function is a string.
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

# The input() function with an argument
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")

# int() and float() functions
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# input() and type casting
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

# Strings Operators
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

# String Replication
# The * (asterisk) sign, when applied to a string and number (or a number and string, as it remains commutative in this position) becomes a replication operator:
"James" * 3 # "JamesJamesJames"
3 * "an" # "ananan"
5 * "2" (or "2" * 5) # "22222" (not 10!)

# This simple program "draws" a rectangle, making use of an old operator (+) in a new role:

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# str(): convert a number into a string
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))
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
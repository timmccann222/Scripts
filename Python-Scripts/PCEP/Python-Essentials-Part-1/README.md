# Python Essentials 1 (Aligned with PCEP-30-02)

## Module 2

### Literals

1. **Literals** are notations for representing some fixed values in code. Python has various types of literals - for example, a literal can be a number (numeric literals, e.g., `123`), or a string (string literals, e.g., "I am a literal.").

2. The **binary system** is a system of numbers that employs *2* as the base. Therefore, a binary number is made up of 0s and 1s only, e.g., `1010` is *10* in decimal.

Octal and hexadecimal numeration systems, similarly, employ *8* and *16* as their bases respectively. The hexadecimal system uses the decimal numbers and six extra letters.

3. **Integers** (or simply ints) are one of the numerical types supported by Python. They are numbers written without a fractional component, e.g., `256`, or `-1` (negative integers).

4. **Floating-point** numbers (or simply floats) are another one of the numerical types supported by Python. They are numbers that contain (or are able to contain) a fractional component, e.g., `1.27`.

5. To encode an apostrophe or a quote inside a string you can either use the escape character, e.g., `'I\'m happy.'`, or open and close the string using an opposite set of symbols to the ones you wish to encode, e.g., `"I'm happy."` to encode an apostrophe, and `'He said "Python", not "typhoon"'` to encode a (double) quote.

6. **Boolean** values are the two constant objects `True` and `False` used to represent truth values (in numeric contexts `1` is `True`, while `0` is `False`.

7. There is one more, special literal that is used in Python: the `None` literal. This literal is a so-called `NoneType` object, and it is used to represent the **absence of a value**.

### Operators

1. An **expression** is a combination of values (or variables, operators, calls to functions ‒ you will learn about them soon) which evaluates to a certain value, e.g., `1 + 2`.

2. **Operators** are special symbols or keywords which are able to operate on the values and perform (mathematical) operations, e.g., the `*` operator multiplies two values: `x * y`.

3. Arithmetic operators in Python: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (classic division ‒ always returns a float), `%` (modulus ‒ divides left operand by right operand and returns the remainder of the operation, e.g., `5 % 2 = 1`), `**` (exponentiation ‒ left operand raised to the power of right operand, e.g., `2 ** 3 = 2 * 2 * 2 = 8`), `//` (floor/integer division ‒ returns a number resulting from division, but rounded down to the nearest whole number, e.g., `3 // 2.0 = 1.0`)

4. A **unary** operator is an operator with only one operand, e.g., `-1`, or `+3`.

5. A **binary** operator is an operator with two operands, e.g., `4 + 5`, or `12 % 5`.

6. Some operators act before others – the **hierarchy of priorities**:

** the `**` operator (exponentiation) has the highest priority;
** then the unary `+` and `-` (note: a unary operator to the right of the exponentiation operator binds more strongly, for example: `4 ** -1` equals `0.25`)
** then `*`, `/`, `//`, and `%`;
** and, finally, the lowest priority: the binary `+` and `-`.

7. Subexpressions in **parentheses** are always calculated first, e.g., `15 - 1 * (5 * (1 + 2)) = 0`.

8. The **exponentiation** operator uses **right-sided binding**, e.g., `2 ** 2 ** 3 = 256`.

### Variables

1. A **variable** is a named location reserved to store values in the memory. A variable is created or initialized automatically when you assign a value to it for the first time. (2.1.4.1)

2. Each variable must have a unique name - an **identifier**. A legal identifier name must be a non-empty sequence of characters, must begin with the underscore(`_`), or a letter, and it cannot be a Python keyword. The first character may be followed by underscores, letters, and digits. Identifiers in Python are case-sensitive. (2.1.4.1)

3. Python is a **dynamically-typed** language, which means you don't need to declare variables in it. (2.1.4.3) To assign values to variables, you can use a simple assignment operator in the form of the equal (`=`) sign, i.e., `var = 1`.

4. You can also use **compound assignment operators** (shortcut operators) to modify values assigned to variables, e.g., `var += 1`, or `var /= 5 * 2`. (2.1.4.8)

5. You can assign new values to already existing variables using the assignment operator or one of the compound operators, e.g.: (2.1.4.5)

```python
var = 2
print(var)

var = 3
print(var)

var += 1
print(var)
```

6. You can combine text and variables using the + operator, and use the print() function to output strings and variables, e.g.: (2.1.4.4)

```python
var = "007"
print("Agent " + var)
```

## Module 3

### User Input

1. The `print()` function sends data to the console, while the `input()` function gets data from the console.

2. The `input()` function comes with an optional parameter: **the prompt string**. It allows you to write a message before the user input, e.g.:

```python
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")
```

3. When the `input()` function is called, the program's flow is stopped, the prompt symbol keeps blinking (it prompts the user to take action when the console is switched to input mode) until the user has entered an input and/or pressed the *Enter* key.

You can test the functionality of the `input()` function in its full scope locally on your machine. For resource optimization reasons, we have limited the maximum program execution time in Edube to a few seconds. Go to Sandbox, copy-paste the above snippet, run the program, and do nothing - just wait a few seconds to see what happens. Your program should be stopped automatically after a short moment. Now open IDLE, and run the same program there - can you see the difference?

Tip: the above-mentioned feature of the `input()` function can be used to prompt the user to end a program. Look at the code below:

```python
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")
```

3. The result of the `input()` function is a string. You can add strings to each other using the concatenation (`+`) operator. Check out this code:

```python
num_1 = input("Enter the first number: ") # Enter 12
num_2 = input("Enter the second number: ") # Enter 21

print(num_1 + num_2) # the program returns 1221
```

4. You can also multiply (`*`- replication) strings, e.g.:

```python
my_input = input("Enter something: ") # Example input: hello
print(my_input * 3) # Expected output: hellohellohello
```

### Decision Making

1. The **comparison** (or the so-called relational) operators are used to compare values. The table below illustrates how the comparison operators work:

```
Operator	Description	
==	        returns if operands' values are equal, and False otherwise	
!=	        returns True if operands' values are not equal, and False otherwise	
>	        True if the left operand's value is greater than the right operand's value, and False otherwise	
<	        True if the left operand's value is less than the right operand's value, and False otherwise
≥	        True if the left operand's value is greater than or equal to the right operand's value, and False otherwise	
≤	        True if the left operand's value is less than or equal to the right operand's value, and False otherwise	
```

2. When you want to execute some code only if a certain condition is met, you can use a conditional statement:

** a single if statement, e.g.:

```python
x = 10

if x == 10: # condition
    print("x is equal to 10")  # Executed if the condition is True.
```

** a series of if statements, e.g.:

```python
x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.
```

Each if statement is tested separately.

** an if-else statement, e.g.:

```python
x = 10

if x < 10:  # Condition
    print("x is less than 10")  # Executed if the condition is True.

else:
    print("x is greater than or equal to 10")  # Executed if the condition is False.
```

** a series of if statements followed by an else, e.g.:

```python
x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("else will be executed")
```

Each if is tested separately. The body of else is executed if the last if is False.

** The if-elif-else statement, e.g.:

```python
x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")
```

If the condition for if is False, the program checks the conditions of the subsequent elif blocks - the first elif block that is True is executed. If all the conditions are False, the else block will be executed.

** Nested conditional statements, e.g.:

```python
x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")
```

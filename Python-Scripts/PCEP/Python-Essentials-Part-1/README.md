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

### Looping

There are two types of loops in Python: `while` and `for`:

* the `while` loop executes a statement or a set of statements as long as a specified boolean condition is true, e.g.:

```python
# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1
```

* the `for` loop executes a set of statements many times; it's used to iterate over a sequence (e.g., a list, a dictionary, a tuple, or a set - you will learn about them soon) or other objects that are iterable (e.g., strings). You can use the `for` loop to iterate over a sequence of numbers using the built-in `range` function. Look at the examples below:

```python
# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
```

2. You can use the `break` and `continue` statements to change the flow of a loop:

* You use `break` to exit a loop, e.g.:

```python
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")
```

You use `continue` to skip the current iteration, and continue with the next iteration, e.g.:

```python
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")
```

3. The `while` and `for` loops can also have an `else` clause in Python. The `else` clause executes after the loop finishes its execution as long as it has not been terminated by `break`, e.g.:

```python
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")
```

4. The `range()` function generates a sequence of numbers. It accepts integers and returns range objects. The syntax of `range()` looks as follows: `range(start, stop, step)`, where:

* `start` is an optional parameter specifying the starting number of the sequence (0 by default)
* `stop` is an optional parameter specifying the end of the sequence generated (it is not included),
* and `step` is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)

Example code:

```python
for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2
```

### Logical and bitwise operators

1. Python supports the following logical operators:

* `and` → if both operands are true, the condition is true, e.g., `(True and True)` is `True`,
* `or` → if any of the operands are true, the condition is true, e.g., `(True or False)` is `True`,
* `not` → returns false if the result is true, and returns true if the result is false, e.g., `not True` is `False`.

2. You can use bitwise operators to manipulate single bits of data. The following sample data:

* `x = 15`, which is `0000 1111` in binary,
* `y = 16`, which is `0001 0000` in binary.

will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:

* `&` does a bitwise and, e.g., `x & y = 0`, which is `0000 0000` in binary,
* `|` does a bitwise or, e.g., `x | y = 31`, which is `0001 1111` in binary,
* `˜`  does a bitwise not, e.g., `˜ x = 240*`, which is `1111 0000` in binary,
* `^` does a bitwise xor, e.g., `x ^ y = 31`, which is `0001 1111` in binary,
* `>>` does a bitwise right shift, e.g., `y >> 1 = 8`, which is `0000 1000` in binary,
* `<<` does a bitwise left shift, e.g., `y << 3 = `, which is `1000 0000` in binary,

* `-16` (decimal from signed 2's complement) -- read more about the Two's complement operation.

### Lists

1. The **list is a type of data** in Python used to **store multiple objects**. It is an **ordered and mutable collection** of comma-separated items between square brackets, e.g.:

```python
my_list = [1, None, True, "I am a string", 256, 0]
```

2. Lists can be **indexed and updated**, e.g.:

```python
my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']
```

3. Lists can be **nested**, e.g.:

```python
my_list = [1, 'a', ["list", 64, [0, 1], False]]
```

You will learn more about nesting in module 3.1.7 - for the time being, we just want you to be aware that something like this is possible, too.

4. List elements and lists can be **deleted**, e.g.:

```python
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list
```

Again, you will learn more about this in module 3.1.6 - don't worry. For the time being just try to experiment with the above code and check how changing it affects the output.

5. Lists can be **iterated** through using the for loop, e.g.:

```python
my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)
```

6. The `len()` function may be used to **check the list's length**, e.g.:

```python
my_list = ["white", "purple", "blue", "yellow", "green"]
print(len(my_list))  # outputs 5

del my_list[2]
print(len(my_list))  # outputs 4
```

7. A typical **function** invocation looks as follows: **result = function(arg)**, while a typical **method** invocation looks like this:`result = data.method(arg)`.

8. You can use the `sort()` method to sort elements of a list, e.g.:

```python
lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst)  # outputs: [1, 2, 3, 4, 5]
```

9. There is also a list method called `reverse()`, which you can use to reverse the list, e.g.:

```python
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]
```

10. If you have a list `l1`, then the following assignment: `l2 = l1` does not make a copy of the `l1` list, but makes the variables `l1` and `l2` **point to one and the same list in memory**. For example:

```python
vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']
```

12. If you want to copy a list or part of the list, you can do it by performing **slicing**:

```python
colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list
```

13. You can use **negative indices** to perform slices, too. For example:

```python
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']
```

14. The `start` and `end` parameters are **optional** when performing a slice: `list[start:end]`, e.g.:

```python
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]
```

15. You can **delete slices** using the del instruction:

```python
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []
```

16. You can test if some items **exist in a list or not** using the keywords `in` and `not in`, e.g.:

```python
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False
```

17. **List comprehension** allows you to create new lists from existing ones in a concise and elegant way. The syntax of a list comprehension looks as follows:

```python
[expression for element in list if conditional]
```

which is actually an equivalent of the following code:

```python
for element in list:
    if conditional:
        expression
```

Here's an example of a list comprehension - the code creates a five-element list filled with with the first five natural numbers raised to the power of 3:

```python
cubed = [num ** 3 for num in range(5)]
print(cubed)  # outputs: [0, 1, 8, 27, 64]
```

18. You can use **nested lists** in Python to create **matrices** (i.e., two-dimensional lists). For example:

```python
# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'
```

19. You can nest as many lists in lists as you want, and therefore create n-dimensional lists, e.g., three-, four- or even sixty-four-dimensional arrays. For example:

```python
# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
```

## Module 4

### Functions

1. A **function** is a block of code that performs a specific task when the function is called (invoked). You can use functions to make your code reusable, better organized, and more readable. Functions can have parameters and return values.

2. There are at least four basic types of functions in Python:

* built-in functions which are an integral part of Python (such as the print() function). You can see a complete list of Python built-in functions at https://docs.python.org/3/library/functions.html.
* the ones that come from pre-installed modules (you'll learn about them in the Python Essentials 2 course)
* user-defined functions which are written by users for users - you can write your own functions and use them freely in your code,
* the lambda functions (you'll learn about them in the Python Essentials 2 course.)

3. You can define your own function using the `def` keyword and the following syntax:

```python
def your_function(optional parameters):
    # the body of the function
```

You can define a function which doesn't take any arguments, e.g.:

```python
def message():    # defining a function
    print("Hello")    # body of the function

message()    # calling the function
```

You can define a function which takes arguments, too, just like the one-parameter function below:

```python
def hello(name):    # defining a function
    print("Hello,", name)    # body of the function


name = input("Enter your name: ")

hello(name)    # calling the function
```

### Parameterized Functions & Arguments

1. You can pass information to functions by using parameters. Your functions can have as many parameters as you need.

An example of a one-parameter function:

```python
def hi(name):
    print("Hi,", name)

hi("Greg")
```

An example of a two-parameter function:

```python
def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")
```

An example of a three-parameter function:

```python
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")

address(s, c, p_c)
```

2. You can pass arguments to a function using the following techniques:

* **positional argument passing** in which the order of arguments passed matters (Ex. 1),
* **keyword (named) argument passing** in which the order of arguments passed doesn't matter (Ex. 2),
* a mix of positional and keyword argument passing (Ex. 3).

```python
# Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


# Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

# Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3
```

It's important to remember that **positional arguments mustn't follow keyword arguments**. That's why if you try to run the following snippet:

```python
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error
```

Python will not let you do it by signalling a `SyntaxError`.

### Function Return Results

1. You can use the `return` keyword to tell a function to return some value. The `return` statement exits the function, e.g.:

```python
def multiply(a, b):
    return a * b

print(multiply(3, 4))    # outputs: 12


def multiply(a, b):
    return

print(multiply(3, 4))    # outputs: None
```

2. The result of a function can be easily assigned to a variable, e.g.:

```python
def wishes():
    return "Happy Birthday!"

w = wishes()

print(w)    # outputs: Happy Birthday!
```

Look at the difference in output in the following two examples:

```python
# Example 1
def wishes():
    print("My Wishes")
    return "Happy Birthday"

wishes()    # outputs: My Wishes


# Example 2
def wishes():
    print("My Wishes")
    return "Happy Birthday"

print(wishes())

# outputs: My Wishes
#          Happy Birthday
```

3. You can use a list as a function's argument, e.g.:

```python
def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)

hi_everybody(["Adam", "John", "Lucy"])
```

4. A list can be a function result, too, e.g.:

```python
def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))
```

### Function and Scopes

1. A variable that exists outside a function has a scope inside the function body (Example 1) unless the function defines a variable of the same name (Example 2, and Example 3), e.g.:

Example 1:

```python
var = 2


def mult_by_var(x):
    return x * var


print(mult_by_var(7))    # outputs: 14
```

Example 2:

```python
def mult(x):
    var = 5
    return x * var


print(mult(7))    # outputs: 35
```

Example 3:

```python
def mult(x):
    var = 7
    return x * var


var = 3
print(mult(7))    # outputs: 49
```

2. A variable that exists inside a function has a scope inside the function body (Example 4), e.g.:

Example 4:

```python
def adding(x):
    var = 7
    return x + var


print(adding(4))    # outputs: 11
print(var)    # NameError
```

3. You can use the `global` keyword followed by a variable name to make the variable's scope global, e.g.:

```python
var = 2
print(var)    # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())    # outputs: 5
print(var)    # outputs: 5
```

### Function Recursion

1. A function can call other functions or even itself. When a function calls itself, this situation is known as **recursion**, and the function which calls itself and contains a specified termination condition (i.e., the base case - a condition which doesn't tell the function to make any further calls to that function) is called a **recursive** function.

2. You can use recursive functions in Python to write **clean, elegant code, and divide it into smaller, organized chunks**. On the other hand, you need to be very careful as it might be **easy to make a mistake and create a function which never terminates**. You also need to remember that **recursive calls consume a lot of memory**, and therefore may sometimes be inefficient.

When using recursion, you need to take all its advantages and disadvantages into consideration.

The factorial function is a classic example of how the concept of recursion can be put in practice:

```python
# Recursive implementation of the factorial function.

def factorial(n):
    if n == 1:    # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24
```

### Tuples

1. **Tuples** are ordered and unchangeable (immutable) collections of data. They can be thought of as immutable lists. They are written in round brackets:

```python
my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(my_tuple)

my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(my_list)
```

Each tuple element may be of a different type (i.e., integers, strings, booleans, etc.). What is more, tuples can contain other tuples or lists (and the other way round).

2. You can create an empty tuple like this:

```python
empty_tuple = ()
print(type(empty_tuple))    # outputs: <class 'tuple'>
```

3. A one-element tuple may be created as follows:

```python
one_elem_tuple_1 = ("one", )    # Brackets and a comma.
one_elem_tuple_2 = "one",       # No brackets, just a comma.
```

If you remove the comma, you will tell Python to create a **variable**, not a tuple:

```python
my_tuple_1 = 1, 
print(type(my_tuple_1))    # outputs: <class 'tuple'>

my_tuple_2 = 1             # This is not a tuple.
print(type(my_tuple_2))    # outputs: <class 'int'>
```

4. You can access tuple elements by indexing them:

```python
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
print(my_tuple[3])    # outputs: [3, 4]
```

5. Tuples are **immutable**, which means you cannot change their elements (you cannot append tuples, or modify, or remove tuple elements). The following snippet will cause an exception:

```python
my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
my_tuple[2] = "guitar"    # The TypeError exception will be raised.
```

However, you can delete a tuple as a whole:

```python
my_tuple = 1, 2, 3, 
del my_tuple
print(my_tuple)    # NameError: name 'my_tuple' is not defined
```

### Dictionaries

1. Dictionaries are **unordered**, changeable (mutable), and indexed collections of data. (*In Python 3.6x dictionaries have become ordered by default*).

Each dictionary is a set of key: value pairs. You can create it by using the following syntax:

```python
my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
    }
```

2. If you want to access a dictionary item, you can do so by making a reference to its key inside a pair of square brackets (ex. 1) or by using the `get()` method (ex. 2):

```python
pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # outputs: soil

item_2 = pol_eng_dictionary.get("woda")
print(item_2)    # outputs: water
```

3. If you want to change the value associated with a specific key, you can do so by referring to the item's key name in the following way:

```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

pol_eng_dictionary["zamek"] = "lock"
item = pol_eng_dictionary["zamek"]    
print(item)  # outputs: lock
```

4. To add or remove a key (and the associated value), use the following syntax:

```python
phonebook = {}    # an empty dictionary

phonebook["Adam"] = 3456783958    # create/add a key-value pair
print(phonebook)    # outputs: {'Adam': 3456783958}

del phonebook["Adam"]
print(phonebook)    # outputs: {}
```

You can also insert an item to a dictionary by using the `update()` method, and remove the last element by using the `popitem()` method, e.g.:

```python
pol_eng_dictionary = {"kwiat": "flower"}

pol_eng_dictionary.update({"gleba": "soil"})
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower'}
```

5. You can use the `for` loop to loop through a dictionary, e.g.:

```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for item in pol_eng_dictionary:
    print(item) 

# outputs: zamek
#          woda
#          gleba
```

6. If you want to loop through a dictionary's keys and values, you can use the `items()` method, e.g.:

```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

for key, value in pol_eng_dictionary.items():
    print("Pol/Eng ->", key, ":", value)
```

7. To check if a given key exists in a dictionary, you can use the `in` keyword:

```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

if "zamek" in pol_eng_dictionary:
    print("Yes")
else:
    print("No")
```

8. You can use the `del` keyword to remove a specific item, or delete a dictionary. To remove all the dictionary's items, you need to use the `clear()` method:

```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

print(len(pol_eng_dictionary))    # outputs: 3
del pol_eng_dictionary["zamek"]    # remove an item
print(len(pol_eng_dictionary))    # outputs: 2

pol_eng_dictionary.clear()   # removes all the items
print(len(pol_eng_dictionary))    # outputs: 0

del pol_eng_dictionary    # removes the dictionary
```

9. To copy a dictionary, use the `copy()` method:

```python
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }

copy_dictionary = pol_eng_dictionary.copy()
```

### Exceptions

1. In Python, there is a distinction between two kinds of errors:

* **syntax errors** (parsing errors), which occur when the parser comes across a statement that is incorrect. For example:
Trying to execute the following line:

```python
print("Hello, World!)
```

will cause a *SyntaxError*, and result in the following (or similar) message being displayed in the console:

```
  File "main.py", line 1

    print("Hello, World!)
                        ^
SyntaxError: EOL while scanning string literal
```

Pay attention to the arrow – it indicates the place where the Python parser has run into trouble. In our case, it's the missing double quote. Did you notice it?

* **exceptions**, which occur even when a statement/expression is syntactically correct; these are the errors that are detected during execution when your code results in an error which is not *uncoditionally fatal*. For example:
Trying to execute the following line:

```python
print(1/0)
```

will cause a *ZeroDivisionError* exception, and result in the following (or similar) message being displayed in the console:

```
Traceback (most recent call last):
  File "main.py", line 1, in 
    print(1/0)
ZeroDivisionError: division by zero
```

Pay attention to the last line of the error message – it actually tells you what happened. There are many different types of exceptions, such as *ZeroDivisionError*, *NameError*, *TypeError*, and many more; and this part of the message informs you of what type of exception has been raised. The preceding lines show you the context in which the exception has occured.

2. You can "catch" and handle exceptions in Python by using the try-except block. So, if you have a suspicion that any particular snippet may raise an exception, you can write the code that will gracefully handle it, and will not interrupt the program. Look at the example:

```python
while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")
```

The code above asks the user for input until they enter a valid integer number. If the user enters a value that cannot be converted to an int, the program will print `Warning: the value entered is not a valid number. Try again...`, and ask the user to enter a number again. What happens in such a case?

* The program enters the while loop.
* The `try` block/clause is executed. The user enters a wrong value, for example: hello!.
* An exception occurs, and the rest of the `try` clause is skipped. The program jumps to the `except` block, executes it, and then continues running after the *try-except* block. If the user enters a correct value and no exception occurs, the subsequent instructions in the *try* block are executed.

3. You can handle multiple exceptions in your code block. Look at the following examples:

```python
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except ValueError:
        print("Wrong value.")
    except ZeroDivisionError:
        print("Sorry. I cannot divide by zero.")
    except:
        print("I don't know what to do...")
```

You can use multiple except blocks within one try statement, and specify particular exception names. If one of the `except` branches is executed, the other branches will be skipped. Remember: you can specify a particular built-in exception only once. Also, don't forget that the **default** (or generic) exception, that is the one with no name specified, should be placed **at the bottom of the branch** (use the more specific exceptions first, and the more general last).

You can also specify and handle multiple built-in exceptions within a single except clause:

```python
while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError):
        print("Wrong value or No division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")
```

4. Some of the most useful Python built-in exceptions are: *ZeroDivisionError*, *ValueError*, *TypeError*, *AttributeError*, and *SyntaxError*. One more exception that, in our opinion, deserves your attention is the KeyboardInterrupt exception, which is raised when the user hits the interrupt key (CTRL-C or Delete). Run the code above and hit the key combination to see what happens.

To learn more about the Python built-in exceptions, consult the official Python documentation.

5. Last but not least, you should remember about testing and debugging your code. Use such debugging techniques as *print* debugging; if possible – ask someone to read your code and help you to find bugs in it or to improve it; try to isolate the fragment of code that is problematic and susceptible to errors: **test your functions** by applying predictable argument values, and try to **handle** the situations when someone enters wrong values; **comment out** the parts of the code that obscure the issue. Finally, take breaks and come back to your code after some time with a fresh pair of eyes.
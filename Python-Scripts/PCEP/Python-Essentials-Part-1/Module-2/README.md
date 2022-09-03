# Module 2 - Labs

## 2.1.1.6 LAB - print() Function

In your first lab:

* Use the `print()` function to print the line `Hello, Python!` to the screen. Use double quotes around the string;
* Having done that, use the `print()` function again, but this time print your first name;
* Remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?
* Then, remove the parentheses, put back the double quotes, and run your code again. What kind of error is thrown this time?
* Experiment as much as you can. Change double quotes to single quotes, use multiple print() functions on the same line, and then on different lines. See what happens.

Solution script: `hello_python_lab.py`

## 2.1.1.18 LAB - print() Function Arguments

Modify the first line of code in the editor, using the `sep` and `end` keywords, to match the expected output. Use the two `print()` functions in the editor. Don't change anything in the second `print()` invocation.

**Expected output**: `Programming***Essentials***in...Python`

Solution script: `print_function_args_lab.py`

## 2.1.1.19 LAB - print() Function Formatting

We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments. Feel free to modify any part of the code, but there is one condition - learn from your mistakes and draw your own conclusions.

Try to:

* minimize the number of `print()` function invocations by inserting the `\n` sequence into the strings
* make the arrow twice as large (but keep the proportions)
* duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: `"string" * 2` will produce `"stringstring"` (we'll tell you more about it soon).
* remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
* do the same with some of the parentheses;
* change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
* replace some of the quotes with apostrophes; watch what happens carefully.

Solution script: `print_function_format_lab.py`

## 2.2.1.11 LAB - print() Function Newline 

Write a one-line piece of code, using the `print()` function, as well as the newline and **escape characters**, to match the expected result outputted on three lines.

**Expected output**:
```
"I'm"
""learning""
"""Python"""
```

Solution script: `print_function_newline_lab.py`

## 2.4.1.7 LAB - Variables

Here is a short story:

Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

Your task is to:

* create the variables: `john`, `mary`, and `adam`;
* assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
* having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
* now create a new variable named `total_apples` equal to addition of the three former variables.
* print the value stored in `total_apples` to the console;
* experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., `+`, `-`, `*`, `/`, `//`, etc.). Try to print a string and an integer together on one line, e.g., `"Total number of apples:"` and total_apples.

Solution script: `variables_lab.py`

## 2.4.1.9 LAB - Miles and Kilometers

Miles and kilometers are units of length or distance.

Bearing in mind that `1` mile is equal to approximately `1.61` kilometers, complete the program in the editor so that it converts:

* miles to kilometers;
* kilometers to miles.

Do not change anything in the existing code. Write your code in the places indicated by `###`. Test your program with the data we've provided in the source code.

Pay particular attention to what is going on inside the `print()` function. Analyze how we provide multiple arguments to the function, and how we output the expected data.

Note that some of the arguments inside the `print()` function are strings (e.g., `"miles is"`, whereas some other are variables (e.g., `miles`).

**Expected output**:
```
7.38 miles is 11.88 kilometers
12.25 kilometers is 7.61 miles
```

Solution script: `miles_kilometers_lab.py`

## 2.4.1.10 LAB - Evaluate Expression

Take a look at the code in the editor: it reads a `float` value, puts it into a variable named `x`, and prints the value of a variable named `y`. Your task is to complete the code in order to evaluate the following expression:

```
3x^3 - 2x^2 + 3x - 1
```

The result should be assigned to `y`.

Remember that classical algebraic notation likes to omit the multiplication operator - you need to use it explicitly. Note how we change data type to make sure that `x` is of type `float`.

Keep your code clean and readable, and test it using the data we've provided, each time assigning it to the `x` variable (by hardcoding it). Don't be discouraged by any initial failures. Be persistent and inquisitive.

**Sample input**:

```
x = 0
x = 1
x = -1
```

**Expected Output**:

```
y = -1.0
y = 3.0
y = -9.0
```

Solution script: `evaluate_expression_lab.py`

## 2.6.1.9 LAB - Evaluate the results of four basic arithmetic operations

Your task is to complete the code in order to evaluate the results of four basic arithmetic operations.

The results have to be printed to the console.

You may not be able to protect the code from a user who wants to divide by zero. That's okay, don't worry about it for now.

Solution script: `user_input_arithmetic_lab.py`

## 2.6.1.10 LAB - Evaluate Expression

Your task is to complete the code in order to evaluate the following expression: `1/((x+(1/(x+(1/(x+1/x))))))`.

The result should be assigned to `y`. Be careful - watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.

You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.

**Sample input**: `1`

**Expected output**:
```
y = 0.6000000000000001
```

**Sample input**: `10`

**Expected output**:
```
y = 0.09901951266867294
```

**Sample input**: `100`

**Expected output**:
```
y = 0.009999000199950014
```

**Sample input**: `-5`

**Expected output**:
```
y = -0.19258202567760344
```

Solution script: `user_input_expression_lab.py`

## 2.6.1.11 LAB - Evaluate End Time

Your task is to prepare a simple code able to evaluate the **end time** of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

For example, if an event starts at **12:17** and lasts **59 minutes**, it will end at **13:16**.

Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.

Test your code carefully. Hint: using the `%` operator may be the key to success.

**Sample input**:

```
12
17
59
```

**Expected output**: `13:16`

**Sample input**:
```
23
58
642
```

**Expected output**: `10:40`

**Sample input**:
```
0
1
2939
```

**Expected output**: `1:0`

Solution script: `user_input_time_lab.py`
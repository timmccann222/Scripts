# variables are used to store the results of operations, in order to use them in other operations, and so on.
# The PEP 8 -- Style Guide for Python Code recommends the following naming convention for variables and functions in Python:
# var, my_var, myVariable
var = 1
print(var)

# multiple variable declarations
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

# combine text and variables using the + operator
var = "3.8.5"
print("Python version: " + var)

# Assigning a new value to an already existing variable
var = 1
print(var)
var = var + 1
print(var)
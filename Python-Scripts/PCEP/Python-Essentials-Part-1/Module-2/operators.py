# An operator is a symbol of the programming language, which is able to operate on the values.

# Addition
print(2+2) 
print(-4 + 4)
print(-4. + 8)

# Subtraction
print(-4 - 4)
print(4. - 8)

# Unary Operators
print(-1.1)
print(+2)

# Exponentiation
# when both ** arguments are integers, the result is an integer, too;
# when at least one ** argument is a float, the result is a float, too.
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# Multiplication
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

# Division
# The result produced by the division operator is always a float
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# Integer division
# The results are always rounded and rounding always goes to the lesser integer
# It still conforms to the integer vs. float rule.
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

# Modulo
# The result of the operator is a remainder left after the integer division
print(14 % 4)
print(12 % 4.5)

# Parentheses
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# Shortcut Operators: variable op= expression
i += 2 * j # i = i + 2 * j
var /= 2 # var = var / 2
rem %= 10 # rem = rem % 10
j -= (i + var + rem) # j = j - (i + var + rem)
x **= 2 # x = x ** 2
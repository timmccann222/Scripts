# Logical Expressions
# Example 1:
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))

# De Morgan's laws.
# The negation of a conjunction is the disjunction of the negations.
not (p and q) == (not p) or (not q)
# The negation of a disjunction is the conjunction of the negations.
not (p or q) == (not p) and (not q)

# Bitwise operators
# & (ampersand) - bitwise conjunction;
# | (bar) - bitwise disjunction;
# ~ (tilde) - bitwise negation;
# ^ (caret) - bitwise exclusive or (xor).

# Binary left shift and binary right shift
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

# Exercise 1
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

# Exercise 2
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
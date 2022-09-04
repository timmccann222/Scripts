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
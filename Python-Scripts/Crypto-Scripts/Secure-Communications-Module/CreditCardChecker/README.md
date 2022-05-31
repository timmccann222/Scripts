# Lab 9 - Credit Card Validator

In this lab I was required to use the Luhn Algorithm to check if a credit card number is valid. The Luhn Algorithm is a
checksum formula used to validate a variety of identification number and is used by some credit card companies to distinguish
between valid credit card numbers and from a random selection of numbers. There are plenty of websites that explain how
the Luhn Algorithm works. The following websites gives a good example of how the luhn algorithm works:

              https://www.rosettacode.org/wiki/Luhn_test_of_credit_card_numbers

              https://www.freeformatter.com/credit-card-number-generator-validator.html

Valid card numbers must be able to pass the following test in order to be valid.

1. Reverse the order of the digits.
2. Take each value at an odd position and add them together
3. Take each value at an even position and multiply them by 2, then add them together.
4. Add the sum of both the values located at the even and odd positions, then mod by 10.
5. If the mod 10 results in a value of 0 then the card number is valid.

The function **luhnAlgorithm()** takes in a string and converts it to a list of integers. This function then reverses the 
string, takes each value in the odd position in the list and adds them. The function then takes each value at the even 
position, multiplies them by two, then adds them together. Finally, both values are added together and then mod10 is used.
If the remaining value is zero, the the card is valid.

The function **cardVendor()** checks the vendor of the card. I imported the **re** module. The card number is taken into 
the function as a string. A python dictionary was created which held Regular Expressions (Regex) as keys and the type of 
card name as the value. I use a for loop to place each key in  the match function and check if the first two digits of 
the card number match any of the patterns. If it does then a message is printed saying which type of card it is. If it  
isn't, then a message is printed saying which type of card it isn't.

The function **validateCreditCard()** is used to call the above functions.

The function **ValidateCreditCard()** is used to validate a credit card using the luhn algorithm. 

The function **RandomCreditCardGenerator()** is incomplete.
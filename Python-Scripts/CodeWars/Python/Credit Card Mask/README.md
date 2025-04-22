# Credit Card Mask

## Instructions

Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into `'#'`.

```
Examples (input --> output):
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "####################################man!"
```

## Solution

1. Find the length of the string using the `len()` function. If it is less than or equal to 4, return the string.
2. If the string length is greater than 4, find the number of **additional** characters in the string, minus the 4 characters at the end, and store the result in a variable titled `string_len`.
3. Use the `string_len` variable to multiply `#` to generate a hash string based on the number of additional characters. This new value can then be stored in a variable titled `masked_part`
4. Use string slicing `[-4:]` to return the last 4 characters of the string and store it in a variable titled `visible_part`.
5. Combine `masked_part` and `visible_part` values together.

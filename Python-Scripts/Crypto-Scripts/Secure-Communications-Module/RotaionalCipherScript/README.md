# Lab 5: Intro to Python with Pycharm

This python script is used to brute force the rotational ciphers **ROT5**, **ROT13** and **ROT47**. The script works
by using the ASCII table chart to match characters to their decimal equivalent. The base value specifies where the 
first character in the rotation begins and the offset value specifies how many characters are used in the cipher. The 
cipher text is rotated using the below piece of code:

```python 
chr(base + (((ord(y)-base) + x) % offset))
```

Working from the inside out, the first equation is to minus the base value from the Unicode code point of the character
that was retrieved using the ord() function. eg: ```python ord(a) = 97 - 97 = 0```Next, add the variable **x** (rotation 
shift value), eg: 13 + 0 = 13. Next perform modulus operation with the offset value eg: 13 % 26 = 13. The modulus operation
returns the shift to the beginning. Finally add the base value and parse it to a character.

 
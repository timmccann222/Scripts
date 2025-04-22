# Split Strings

## Instructions

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

```
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
```

## Solution

1. Use modulus `%` to check if the string length is **not** divisible by 2. If not, then add an underscore `_` string to the end of the string.
2. Create an empty list titled `pairs` to store the pair of characters from the string.
3. Use a `for` loop to iterate over the string, starting at position 0 and ending at the position equal to length of the string. Set the step count to 2 to move in steps of 2.
4. Use string slicing that starts at index i and goes up to (but not including) i + 2. This gives you a 2-character substring.
5. Append each character pair to the `pairs` list.

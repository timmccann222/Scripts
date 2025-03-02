# Count by X

## Scenario

Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).

Examples

```
x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
x = 2, n = 5  --> [2,4,6,8,10]
```

## Solution 1 - For Loop

Used a for loop and appended to an array.

## Solution 2 - List Comprehension

Instead of using a for loop and `.append()`, the list comprehension `[x * y for y in range(1, n + 1)]` does the same thing in a single line. This makes the function cleaner and more Pythonic.

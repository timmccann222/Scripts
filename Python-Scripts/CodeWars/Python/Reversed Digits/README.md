# Reversed Digits

## Scenario
 
 Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
 
 Example (Input => Output):
 
 ```
 35231 => [1,3,2,5,3]
 0     => [0]
 ```
 
 ## Solution
 
 You can achieve this by converting the number to a string, reversing the string, and then converting each character back into an integer to form a list. 
 
 ```python
 [int(digit) for digit in str(number)[::-1]]
 ```
 
 1. Take the provided number and convert it to a string using `str(number)`.
 2. Reverse the string using python string slicing technique `[::-1]`.
 
 ```python
 # start: where the slice starts
 # end: where the slice ends
 # step: the number of indices to jump at a time
 
 # syntax
 string[start:end:step]
 
 # Output: "Pyt"
 text = "Python"
 print(text[0:3])  
 
 # Output: "Pto"
 text = "Python"
 print(text[::2])
 
 # negative indices
 text = "Python"
 print(text[-1])  # Output: "n"
 print(text[-3:-1])  # Output: "ho"
 
 # reverse string
 [::-1]
 ```
 
 * Use list comprehension to iterate over each character and return a final list of the reversed number `[int(digit) for digit in str(number)[::-1]]`
 
 
 ## Example
 
 Let's say number = 35231:

 ```
 str(number) -> "35231"
 
 str(number)[::-1] -> "13253"
 
 [int(digit) for digit in "13253"]:
 
 Converts '1' to 1
 
 Converts '3' to 3
 
 Converts '2' to 2
 
 Converts '5' to 5
 
 Converts '3' to 3
```

# Counting Sheep

Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

```
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
```

The correct answer would be 17.

**Hint**: Don't forget to check for bad values like null/undefined

## Approach

I used the list `count` method, which is more efficient than sum, as well as being more explicit about the intent. The `.count(True)` is a built-in list method that counts how many times **True** appears in the list. Since True is internally represented as 1 in Python (`bool` is a subclass of int), `.count(True)` correctly counts only the True values and ignores False, None, or other values.

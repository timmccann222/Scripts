# Python Strings

## Slicing Strings

Specify the start index and the end index, separated by a colon, to return a part of the string `[start:end]`.

Get the characters from position 2 to position 5 (not included):
```python
b = "Hello, World!"
print(b[2:5])
```

**Slice From the Start**: By leaving out the start index, the range will start at the first character:

Get the characters from the start to position 5 (not included):
```python
b = "Hello, World!"
print(b[:5])
```

**Slice To the End**: By leaving out the end index, the range will go to the end:

Get the characters from position 2, and all the way to the end:
```python
b = "Hello, World!"
print(b[2:])
```

**Negative Indexing**: Use negative indexes to start the slice from the end of the string:

Get the characters:
* From: "o" in "World!" (position -5)
* To, but not included: "d" in "World!" (position -2):
```python
b = "Hello, World!"
print(b[-5:-2])
```

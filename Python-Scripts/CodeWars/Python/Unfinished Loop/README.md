# Unfinished Loop

## Scenario

Unfinished Loop - Bug Fixing #1
Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!

```
def create_array(n):
    res=[]
    i=1
    while i<=n: res+=[i]
    return res
```

## Solution

The `while` loop condition where `i<=n` will always be true since the variable `i` is never incremented. This can be fixed by incrementing the variable `i` (i.e. `i+=1`)

```
# old code
while i<=n: res+=[i]

# new code
while i<=n: res+=[i]; i+=1
```


# Decoding Cipher

For the Anonymous Playground THM challenge, there was an encoded message that needed to be decoded.

Encoded Message: `hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN`.

Hint: `'zA' = 'a'`.

Based on the hint, if you change the letters to their **ordered numerical position** in the **alphabet** and added them together, then you would get a new value which would represent the ordered numerical position of another letter in the alphabet (see examples below).

```
# EXAMPLE 1
'z' = 26 # 26th letter in the alphabet
'A' = 1 # 1st letter in the alphabet

(26 + 1) % 26 = 1 = 'a'

# EXAMPLE 2
'h' = 8
'E' = 5

(8 + 5) % 26 = 13 = 'm'

N.B. Mod (i.e. '%') 26 is used since there are only 26 letters in the alphabet.
```

Using this, I created a simple python script to do it with the help of some online sources.
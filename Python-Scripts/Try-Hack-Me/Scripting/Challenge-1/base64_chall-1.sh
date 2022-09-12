# TryHackMe: https://tryhackme.com/room/scripting
#!/bin/bash

# Backticks ` are discouraged. Use $(...) instead.
flag=$(<b64.txt) 
# If the file contains one line only, there is no need to iterate over the words in the file.
for i in {1..50}; do
   flag=$(<<<"$flag" base64 --decode) # decode file contents
done
echo "Flag: $flag"
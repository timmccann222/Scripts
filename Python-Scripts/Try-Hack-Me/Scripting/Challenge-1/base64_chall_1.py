# TryHackMe: https://tryhackme.com/room/scripting
import base64 

# base64 decode function
def base64_decode(data):
	decoded = base64.b64decode(data)
	return decoded

# stores flag
flag = ""

# open file in current directory
with open('b64.txt', "r") as f:
	data = f.read()

	for i in range(0,50):
		data = base64_decode(data)
		flag = data

	f.close()
	
print("Flag: ", flag.decode("utf-8"))
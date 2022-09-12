# https://tryhackme.com/room/scripting
import socket
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

def decryption(key, iv, cipher_text, tag):
	# Create AES GCM decryptor object
	decryptor = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend = default_backend()).decryptor()
	# Return decrypted text
	return decryptor.update(cipher_text) + decryptor.finalize()

# Hardcoded for ease
host = "10.10.86.119"
port = 4000
key = b"thisisaverysecretkeyl337" 
iv = b"secureivl337"

# create an INET, STREAMing socket, UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# now connect to the server on port the speciifed port
s.connect((host, port))

# The method sendto() of the Python's socket class, is used to send datagrams to a UDP socket. 
# For sendto() to be used, the socket should not be in already connected state.

# Get Message 1 - Initial Message
s.sendto(b"hello", (host,port))
print("Message 1:\n\n", s.recv(1024), "\n")
# Get Message 2 - Get Key, IV, and Checksum
s.sendto(b"ready", (host,port))
message = s.recv(1024)
print("Message 2:\n\n", message, "\n")
# Convert checksum to hex
checksum = message[104:136].hex() 
print("Checksum: ", checksum, "\n")

while True:
	# get cipher text
	s.sendto(b"final", (host,port))
	cipher_text = s.recv(1024)
	print("Message 3 - Cipher Text:\n\n", cipher_text, "\n")
	# get tag
	s.sendto(b"final", (host,port))
	tag = s.recv(1024)
	print("Message 3 - Tag:\n\n", tag, "\n")
	# decrypt text
	plain_text = decryption(key, iv, cipher_text, tag)
	# confirm checksum
	if hashlib.sha256(plain_text).hexdigest() != checksum:
		continue
	else:
		print("Flag: ", plain_text)
		break
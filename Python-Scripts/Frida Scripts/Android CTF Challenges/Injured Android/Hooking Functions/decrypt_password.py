from Crypto.Cipher import AES
import base64
# private encryption key.
key = b'This is the super secret key 123'
# static initilization vector (iv).
iv = 16 b'\x00'
# base64 decode password
password = base64.b64decode("v/sJpihDC02ckDmLW5Uwiw==")
# Setup cipher AES to use CBC Mode, key and iv.
aes = AES.new(key, AES.MODE_CBC, iv)
# decrypt base64 decoded password with key and iv.
decrypted password = aes.decrypt (password)
# print decrypted password.
print("Decrypted password: " + decrypted_password)

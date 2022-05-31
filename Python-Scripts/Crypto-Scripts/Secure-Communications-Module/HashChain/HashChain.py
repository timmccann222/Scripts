# @author Tim McCann
import hashlib

correct_hash = "c89aa2ffb9edcc6604005196b5f0e0e4" # The hash that needs to be compared.
hashlist = [] # List that holds all the hashes.

seed = "ecsc" # This is the seed given that starts the hash chain.
hash = hashlib.md5(seed.encode()).hexdigest() # This hashes the seed, creating the first hash in the chain.

# While loop that prints out all hashes before there is a match
while hash != correct_hash:
    hash = hashlib.md5(hash.encode()).hexdigest() # hashes the seed hash again.
    hashlist.append(hash) # appends each new hash in the hash chain to a list.
    if(hash == correct_hash): # checks if the hash is correct
        print("Last hash in list: " + hash)
        print("Hash before last hash in list: " + hashlist[-2])
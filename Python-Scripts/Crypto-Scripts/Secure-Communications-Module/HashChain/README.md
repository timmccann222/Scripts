# Lab 8 - Simple Hash Chains

I was given the following scenario for this assignment:

You've registered for an online service that uses hash chains. You've registered as user 'nOOB' and have been given the 
hash chain seed 654e1c2ac6312d8c6441282f155c8ce9. Use the given information to figure out how to authenticate as the user
'ECSC' for the given challenge hash c89aa2ffb9edcc6604005196b5f0e0e4 i.e. Find the hash that hashes to this - This hash 
will be your solution.

The first step is understanding what a hash chain is and how it works. A hash chain is where a hash value is hashed again
and again, forming a chain of hashes. The hash chain **seed** is the first link in the hash chain. You must have the seed in 
order to attack the hash chain. A hash chain seed is the original string that is hashed and can normally be something like
a users password or something. It is impossible to reverse a hash chain and so users are verified by hashing this string
until it matches the same hash that it is compared against.

So, the next step is to find the seed for the given hash chain of the user we want to authenticate as. In the assignment 
brief it is suggested that I figure out how the seed was generated for the user 'nOOB'. The first hash of the chain is 
given so I use the online MD5 Decrypter tool below and enter the given hash seed for user nOOB:

                  https://hashkiller.co.uk/md5-decrypter.aspx

The above website returned the string **'Noob'**. The hash chain seemed to be the user name used but the letters converted 
from uppercase to lowercase and vice versa. Working from this analogy, it was concluded that the seed for the hash chain 
was generated from inverting the letters in a user name from lowercase to uppercase and vice versa. So the seed for the 
user 'ECSC' would be **'ecsc'**. 

The final step was to create a script in python to hash the above seed and return the hash before the hash given for the 
user 'ECSC'. In the script, the seed is hashed and then compared in a while loop to the given hash above. If it matches
then the second last hash in the list before is returned. If it does not match then the hash is simply added to the list 
and then hashed again, creating a new hash to be compared.
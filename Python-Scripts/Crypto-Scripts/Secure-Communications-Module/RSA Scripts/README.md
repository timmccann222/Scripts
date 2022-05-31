# Secure Communications - RSA Labs 
There are 10 RSA challenges that need to be solved using only python. No CTF tools are allowed. The document outlines how 
each challenge was solved and what was learned from solving each challenge.

## RSA Background and Research 
This section goes into detail about the RSA cryptosystem, how RSA works and the topics that are essential to understanding RSA. 
The goal of this section is to build up to understanding RSA in detail by first demonstaring with examples how RSA works,
followed by key topics in RSA and then finally explaining RSA in detail.

The Rivest–Shamir–Adleman (RSA) cryptosystem is one of the first public key cryptosystems and is commonly used for secure 
data transmission. It is a asymmetric encryption and due to it being relatively slow, it is not commonly used to encrypt
user data but is more often used to pass encrypted shared keys for symmetric cryptography. In RSA, the encryption key is 
public and the decryption key is private. 

### RSA encryption works as follows:

Suppose Alice wants to send a secret message to Bob using RSA cryptosystem.

1. Alice first creates her key pair by selecting Two prime numbers which are represented by **p** and **q**. 
So:
             
             p = prime number
             q = prime number

2. Alice next takes the values **p** and **q** and multiplies them which gives you **n**. Also referred to as the modulus, **n**
also gives you the key size in RSA (eg: 1024,2048). So:

             n = p * q
             
3. Alice next figures out the totient of **n** which is equal to p minus 1 multiplied by q minus 1. So:

             ϕ(n) = (p-1)*(q-1)
             
4. Alice now has to choose a value for **e** which is called the exponent because we use it to raise values to the
power of **e**. The value of **e** must be between 1 and the **ϕ(n)**. Also the greatest common divisor (GCD) of **e** has 
to be 1.

5. Finally, Alice finds the value **d**, the private exponent value which is found by taking the inverse of e and doing a modulo function of the 
ϕ(n). So:

             d =  e^-1 % ϕ(n)

The private and public key can be represented with the following number pairs:

             priv key (n,d)
             pub key (n,e)
 
In RSA, encryption works by taking the plaintext and converting it to numbers. Next, the plaintext is put to the power of 
**e** and then modulo **n**. To decrypt ciphertext, the cipher value is taken and raised to the **d** power then modulo **n**. This 
can be seen below:

             plaintext^e % n = ciphertext    (encrypt)
             ciphertext^d % n = plaintext    (decrypt)

### RSA Worked Example:
It is easier to see how RSA works by demonstrating it. Keep in mind that the values that would be commonly used are far
larger than the ones used in the demonstration seen here. So the same steps seen above are applied:

Alice chooses two prime numbers: **p = 3** and **q = 11**.

Alice calculates the modulus(n), which is **n = 33**:
             
             n = p * q
             n = 3 * 11
             n = 33
             
Alice needs to compute her public key(e) and private key(d). We can use the below formula to calculate **e** and **d**:

             1 = d * e % (p - 1)(q - 1)
             1 = d * e % (3 - 1)(11 - 1)
             1 = d * e % 20

Using this formula, we randomly select a value for e that must be less than (p - 1)(q - 1) which is equal to 20. So we choose 
**e = 7** and workout **d** by seeing which value will equal to one, as seen below:

             1 = 1 * 7 % 20
             1 = 7  (incorrect value)
             
             1 = 2 * 7 % 20
             1 = 14 (incorrect value)
             
             1 = 3 * 7 % 20
             1 = 1 (correct value, so d = 3)
             
So, we now know that **e = 7** and **d = 3**.

Assuming Bob has followed a similar process to Alice, Alice shares her public key value (33,7) = (n,e) with Bob. 

Bob wants to send the secret message *20* to Alice, so he calculates:

             c = M ^ e % n
             c = 20 ^ 7 % 33
             c = 26
             
Alice decrypts Bob's message by calculating:

             m = c ^ d % n
             m = 26 ^ 3 % 33
             m = 20

### RSA Topics
It is important to understand these topics, in order to fully grasp how RSA works.

#### RSA Topics - Modulo Division 
This is vital to RSA and other crypto protocols, an is one of the components that secures RSA. Modulo division is simply 
the remainder when two numbers are divided, eg: 5 mod 2 = 1. 

A formal way of stating a remainder after dividing by another number is an equivalence relationship:

             x ≡ y mod z <----> x = k * z + y

The equation basically states that if **x** is equivalent the *remainder* (**y**) after dividing by an *integer* (**z**), 
then **x** can be written like so:

             x = k * z + y    (where k is an integer)
             
An example will make it more clear. If y = 4 and z = 10, then the following values of x will satisfy the above equation:

             x = 4, x = 14, x = 24, .....
             
It is easier to see with calculations:

             x = 0 * 10 + 4
             x = 4
             
             x = 1 * 10 + 4
             x = 14
             
             x = 2 * 10 + 4 
             x = 24 
             
Therefore, **x** can be written like so:

             x = k * 10 + 4
             
Where **k** can be any of the infinite amount of integers. Since there are an infinite amount of values that **x** can take,
we use the equivalence (≡) relationship instead of the equals (=).

There are two important things to note:

1. The remainder **y** (4) remains constant, whatever value **x** takes to satisfy the equation.

2. The remainder **y** value must be in the set of integers **modulo z**.

Zp = {0,1,2,3,4.....p-1} is called the **set of integers modulo p**. It is a set of integers that contains integers from 0 up
until **p-1**.

eg: Z10 = {0,1,2,3,4,5,6,7,8,9}

#### RSA Topics - Multiplicative Inverse and The Greatest Common Denominator (GCD)
A **multiplicative inverse** for **x** is a number that when multiplied by x will equal 1. This is written as x^-1 and is defined
as so: 

            x.x^-1 = 1
            
The GCD between two numbers is the largest integer that will divide both numbers, eg: gcd(4,10) = 2.

An interesting point to note is that if two numbers have a GCD of 1, then the **smaller** of the two numbers has a multiplicative 
inverse in the modulo of the **larger** number. It is expressed in the following equation:

           x ∈ Zp, x^-1 ∈ Zp <----> gcd(x,p) = 1
             
Example: Lets work in the set Z11. the gdc(5,11) = 1. Therefore 5 has a multiplicative inverse (5^-1) in mod 11. This is
shown by the calculation below:
 
           Z11 = {0,1,2,3,4,5,6,7,8,9,10}
           
           5 * 0 mod 9 = remainder of 9
           
           5 * 1 mod 9 = remainder of 5
           
           5 * 2 mod 9 = remiander of 1. This means 2 is the multiplicative inverse of 5 in the set Z11.
           
#### RSA Topics - Prime Numbers
Prime numbers are very important to the RSA algorithm. For any prime number p, every number from 1 up to p-1 has a gcd of
1 with p, and therefore has a multiplicative inverse in modulo p.

#### RSA Topics - Eulers Totient
Eulers Totient is the number of elements that have a multiplicative inverse in a set of modulo integers. The totient is 
denoted using the greek symbol phi ( ϕ ). This brings us to an important equation regarding the totient and prime numbers:

           p ∈ Primes, ϕ(p) = p-1
           
eg: 
           ϕ(7) = |{ 1,2,3,4,5,6 }| = 6
           

## RSA in Detail
With the previous topics covered, it is now possible to describe how RSA works in depth.

RSA is actually a set of two algorithms:

1. **Key Generation**: key generation algorithm.

2. **RSA Function Evaluation**: a function (**F**), that takes as input point **x** and a key **k**, producing either an encrypted 
result or plaintext, depending on the input and the key.

### RSA in Detail - Key Generation
The most complex part of RSA is to generate both the public and private RSA keys. Weak key generation makes RSA very vulnerable to
attack so it must be done correctly. We know from earlier the steps involved for generating these keys so we will now expand
on these steps.

#### Generate P and Q prime numbers (Rabin - Miller Primality Test)
Generating composite numbers or even prime numbers that are close together makes RSA totally insecure.

In order to generate large prime numbers, we select a large random number and check for primeness using the **Rabin-Miller 
primality test**, which quickly determine with a high probability if it's input is a prime.

Thus, two large primes p and q are generated with Rabin Miller.

#### Calculate Modulus(N) 
Calculated by p*q, RSA's security relies upon the fact that given just **n**, there is no known algorithm to efficiently 
determine **n**'s prime factors.

The foundation of RSA's security relies upon the fact that given a composite number, it is considered a **hard problem** to
determine it's prime factors.

#### Calculate ϕ(n)
Calculated by (p-1)(q-1), the reason why RSA becomes vulnerable if one can determine the prime factors of the Modulus is because 
then one can determine the totient.

#### Calculate the Public Key
Normally expressed as **e**, it is a prime number chosen in the range **[ 3, ϕ(n) ]**. The number 3 could lead to security problems 
due to security problems being so small, so in practice, the public key is normally set at **65537**. 

Note that because the public key is prime, it has a high chance of a gcd equal to 1 with **ϕ(n)**. If this is not the case 
we must use another prime number that is not **65537**.

The public key is represented as **(e,n)**.

#### Calculate the Private Key
Due to the public key having a gcd of 1 with ϕ(n), the multiplicative inverse of the public key with respect to ϕ(n) can be effectively
and quickly determined using the **Extended Euclidean Algorithm**. This multiplicative inverse is the private key.

The common notation for expressing the equation for calculating **d** is one of the most important in RSA:

            e*d = 1 % ϕ(n)
            
The private key is expressed as **(d,n)**.

## RSA in Detail - Function Evaluation 
This is the process of Transforming a plaintext message into a ciphertext or vice versa.

**Encryption**: F(m,e) = m ^ e % n = ciphertext

**Decryption**: F(e,d) = c ^ d % n = message

## RSA from Scratch
So there it is, that is RSA!!

I'll provide one more academic example that looks at the process and then we can proceed into the RSA challenge completed.

Keep in mind that as explained earlier, the p and q values are much larger in real world use. We will work with the 
following values:

1. Calculation of Modulus(n) and Totient(ϕ(n)):

                  p = 11, q = 13
                  
                  n = p * q = 143
                  
                  ϕ(n) = (p-1)(q-1) = 120
                  
2. Key Generation:

The public exponent **e** must be less than ϕ(n) and have a GCD of 1 with ϕ(n). There are plenty of numbers to choose from
that satisfy these requirements (we will choose 7), which can be seen below:
 
                   gcd(7,120) = 1
                   gcd(13,120) = 1
                   gcd(17,120) = 1
                   etc....

The private exponent **d** is calculated by finding the inverse of **e** which is 7 with ϕ(n). This can be done quickly with the 
Extended Euclidean Algorithm. We will show this calculation for the sake of understanding the process.

Since we know that the gcd(e, ϕ(n)) = 1, we know that there is a nultiplicative inverse of e in the modulo set of the larger 
number. The following calculation is used to find **d**:

                  Z120 = {0,1,2.....(120-1)}
                  
                  7 * 0 % 120 = 0
                  7 * 1 % 120 = 7 
                  .......
                  7 * 103 % 120 = 1 (correct)
                  
So **d = 103**.

Finally we use the Encryption and Decryption functions with our values above. Our plaintext message is 9:

**Encryption**: m ^ e % n = 97 % 143 = 48 = **ciphertext**

**Decryption**: c ^ d % n = 48 ^ 103 % 143 = 9 = **message**


Can learn more about RSA from the link below:

             https://en.wikipedia.org/wiki/RSA_(cryptosystem)

## Challenge 1 - Encrypt RSA
In this challenge I am given the values **p**,**q**,**n**,**e** and **d**. I am asked to convert the string "RSA isn't really that hard"
using the provided values above. The first step is to convert the string to numerical format, which is done using the function
string2int(). This converts the string to a bytes like object using the hexlify() function. Next the pow(x,y,z) function is used
where x is the number which is to be powered, y which is the number which x is to be powered by and z which
is the number to be used for modulus operation. The pow() function for this challenge looks as follows:

         pow(m,e,n) 
         
The **m** represents the plaintext message, while **e** and **n** represent the respective exponent and modulus provided 
for the challenge. This outputs the answer which is submitted as the flag for the challenge.

Flag: 13309476856206179288137278795001286676504235122200291222905951541015281640474228799375180129564959032261555135231635439690367282451635413048574322588643043250005501837597608399627442074603517951858976430767446724730937928672932493206869274420288717036712376949408229648116702610597844919828482630797157003777363091998366855062763360538948110895070725322039940644906900772757193759215740687066380017485804644723367158972689710477927318380335919282326398046586751715463059075476044138690978986063001880735783893361380726584661054926968590764176030209214513123458853087059980258593405395678238799024217478961749328706800


## Challenge 2 - Decrypt RSA
In this challenge I am asked to decrypt a cipher text using the same values given to me in challenge 1 except with a new ciphertext. 
The same approach is taken as in challenge 1 except the values in the power function are changed. The value m is replaced with c and the 
value **e** is replaced with **d**. The pow() function can now be seen below:

         pow(c,d,n)
         
This reveals the flag: **ZD{Well Done you have decrypted correctly}**

## Challenge 3 - Find Values n, e, and d
In this challenge I am asked to find the values **n**, **e**, and **d** from the provided RSA private key. The private RSA
key consists of the modulus n and the private (or decryption) exponent d, which must be kept secret. p, q, and φ(n) must 
also be kept secret because they can be used to calculate d. In summary, the private  key contains contains the elements 
(n, e, P, E, DP, DQ, InverseQ, D).

To extract these components, from the pycryptodome module, RSA was imported. The function importkey() was used to read in 
the private RSA key and return the components I need to complete the challenge. The list of variables below can be used 
to extract their respective values:

n (integer) – RSA modulus
e (integer) – RSA public exponent
d (integer) – RSA private exponent
p (integer) – First factor of the RSA modulus
q (integer) – Second factor of the RSA modulus
u – Chinese remainder component (p−1mod q)

The values were retrieved and the flag submitted in the requested format. The below link can be used to learn more.

                   https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html 

## Challenge 4 - Decrypt 2 
This challenge gives me a cipher text to decrypt and a private RSA key. It combines the challenges 3 and 2, where i need to
retrieve the components from the private RSA key provided and then decrypt the cipher text. This was achieved using the 
same methods used in challenges 2 and 3.

The flag: **ZD{OK time to move onto some harder stuff}**

## Challenge 5 - Chinese Remainder Algorithm (CRT)
In this challenge, I am given a cipher text to decrypt and a file that contains the components **p**, **q**, **dp**, **dq**, 
**qinv**, and **pinv**. Except for **pinv**, all the new components are part of the RSA private key and are used in the
CRT to improve efficiency and optimize decryption. The new components are calculated as follows:

                  dp = d % (p-1)
                  dq = d % (q-1)
                  qinv = q^-1 % p
                  pinv = p^-1 % q
                  
The problem with RSA is that there is a lot of large computations. The idea behind the CRT optimization is that if we know 
the factorization of the modulus N (which we may if we have the private key), then we can split up the message M into two 
halves (one modulo p, and one modulo q), compute each modulo separately and then recombine them. Since each calculation 
uses a smaller modulus, there is less computation required  The following link: https://www.di-mgt.com.au/crt_rsa.html was 
useful in understanding how to go about using the CRT algorithm in python. The first half of the message and second have 
of the message can be decrypted as follows:

                  m1 = c^dp % p
                  m2 = c^dq % q

Next we calculate h which can be seen below:
                  
                  h = (qinv * (m1-m2)) % p

Finally, the Message is reconstructed using the below calculation:
                  
                  message = m2 + (h * q)
                  
In this challenge, it was possible to get the flag just by using the pow() with the below values:

                  pow(c,dp,p)

This gave the flag: **Those extra private key values are meant to make it easier?**

## Challenge 6 - Decryption Exponent
In this challenge I am given a cipher text to decode but there is no privet **d** exponent provided. In order to decipher 
the given cipher text it is necessary to calculate the private exponent **d**. The private exponent can be calculated by
using the below formula:

                  d =  e^-1 % ϕ(n)
                 
First step is to calculate **phi** of **n**:
                  
                  phi = (p-1)*(q-1)
                  
Next, using a mod inverse and extended euclidean algorithm functions taken from Rosetta Code, the inverse of e mod phi of 
n is found, giving the private exponent **d**. This new private exponent is used to decipher the text as normal giving us the flag.

The flag is: **You are doing very well, you must be starting to understand RSA by now!**

## Challenge 7 - FactorDB 
In this challenge, I am given a cipher text but no **p** and **q** prime numbers which makeup the modulus **n** component.
In the challenge, a hint is given that says *"FactorDB is your friend"*. FactorDB is a factorization database which can be
used to give the factors of n which are **p** and **q**. To retrieve these prime numbers I enter in the modulus to FactorDB
which returns two values, my **p** and **q** prime numbers.

After doing the above, the only steps left were to find the private key exponent **d** as in the previous challenge and 
then retrieve the flag.

The flag is: **Only 4 more challenges to go!**

## Challenge 8 - Ciphertext Length
In this challenge, I am given a hint that says *"what happens if M^e < n?"*. In this scenario, if **M** to the power of **e**
is smaller than **n**, then no modulus takes place. This can be seen more clearly by the below examples where the message
and modulus size are different:

               9 % 5 = 4  (message is bigger than modulus)
               
               5 % 9 = 5  (message is smaller than modulus)

As seen above if the message is smaller then the modulus, then no modulus takes place since 9 does not go into 5 any 
amount of times and so has a remainder of the original message, which in this example is 5. 


All that is needed to recover the message is to find the **e** root of the message. In this case **e** is 3. The cubic 
root of the message can be found by simply putting the cipher text message into FactorDB which returns the cubic root, 
giving the decrypted message. 

The flag is: **We always need to watch the size of our message**

## Challenge 9 - Hastdad (Broadcasting) Attack:
In this challenge, three ciphertexts, public keys and exponents were provided. By reading the article written by Dan Boeh
entitled *"Twenty years of attacks on the RSA crytposystem"*, I discovered that this was a Hastdad attack. If the same message
is encrypted with a different modulus each time but uses the same public exponent value and the encrypted ciphertext for each
message is found, then it is possible to discover the original message using the Guass Algorithm. This link is useful in 
understanding how to crack this RSA Challenge: https://www.di-mgt.com.au/crt.html. The Gauss algorithm is used as follows.
                    
First calculate N which is equal to n1*n2*n3.

Next divide N by each modulus (n1,n2,n3) which provides e.

We now use the e above to find d for each ciphertext so for c1 the d1 = e^-1%n1.

Finally, to get the message we multiply the c, d, and n for each case. This can be seen below:

                    ((c1N1d1) + (c2N2d2) + (c3N3d3)) (mod N)
                    
The answer for this challenge is: Impressive: **small_e_is_the_killer 38247601923468**

## Challenge 10 - RSA Common Modulus Attack:
The following link was useful: https://blog.0daylabs.com/2015/01/17/rsa-common-modulus-attack-extended-euclidean-algorithm/

In this challenge, I am given two ciphertexts (c1,c2), public exponents (e1,e2) and modulus values (n1, n2). The hint for 
the challenge is that the modulus is the same for both ciphertexts, which means that a RSA common modulus attack may be 
possible. First, we need to see if the greatest common denominator (gcd) between both exponents is equal to 1. This was done 
using the gcd() function. This verified that the gcd was 1, which is important for this to work. 

We know that RSA encryption works by putting the message (m) to the power of the public exponent (e) mod the modulus (N)
as seen below:

                    c1 = m^e1 % N 
                    c2 = m^e2 % N
                    
 If we can find a and b such that (e1 * a) + (e2 * b) = 1 then we can decode the plain text as (c1 ^ a) + (c2 ^ b). So 
 we can find *a* and *b* by using the extended euclidean algorithm function, extended_gcd(). This provided me with the 
 values -1 and 21846. Another issue that can happen here is that, in most of these cases, the value of a or b will be negative.
 To fix this this, we find out another value named i, which is the modular multiplicative inverse of c2. 
 Then we can say i^-b = c2^b. To accomplish this the multiplicative modular inverse function was used called mod_inv().
 
 After getting a and b, we can get back the plain text by applying the equation:
 
                   plain = (c1^a) * (c2^b) %N
 
 The flag is: **Only one more to go.. the force is strong with this one!**
 
 ## Challenge 11 - dp Breaks RSA:
 In this challenge, I am given **e**, **n**, **dp** and **c** and asked to decrypt the ciphertext. A quick search on google reveals 
 that this challenge was taken from a PicoCTF 2017 challenge titled Weird RSA. This writeup helps explain how to approach the challenge: 
 https://medium.com/@nicebowlofsoup/picoctf-2017-weirderrsa-writeup-194b30cb3316. 
 
 In order to decrypt an RSA ciphertext, you would need **c**, **d** and **n**. Since we only have c and n, we need to find **d**.
 In this challenge we are given **dp** and we know that **dp = d % (p-1)**. The component dp is used to speed up RSA calculations.
 In the RSA RFC it is stated that **e * dp ≡ 1 (mod p-1)**, which is p's crt exponent. 
 
 In order to calculate **d**, we need p and q. Once we have both factors of n, we can essentially calculate d.We know that 
 *d = e^-1 % ϕ(n)*. So, we need to find **p** and **q** since *ϕ(n) = (p-1)(q-1)*, in order to calculate **d**. 
 
 To find **p** and **q**, we need to find the factors of **n**. Since we have **n**, **e** and **dp**, it is possible to 
 select an arbitrary value (lets say k), which is a multiple of **p**. If we can find a multiple of p such that **a** multiplied
 by **p** for some positive integer that is greater than 1 and the gcd(a,q) = 1, then we can do gcd(a times p, n) = gcd(a times p, p times q)
 to give us p because the only shared factor (greatest number) that divides into the two above values is p.
 
 Once p is found, we can divide **n** by p to give us **q** (since n = p * q). Once we have the factors of n, we can then 
 calculate d, and then decrypt the ciphertext.
 
 The below formula can be used to find **p**:
 
                  ((k ^ (dp*e)) - k) % n
                  
 This is because k ^ (e*dP) = k % p (as e and dp = d % (p−1) are inverses of each other modulo p−1). Once we have **p**, it
 is possible to get q and then create d private exponent. After this, we can decrypt the text.
 
 Flag: **Go take a well earned break.. Happy holidays.**
                  
 
 
 
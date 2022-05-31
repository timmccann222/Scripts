# @author Tim McCann

ciphertext = input('Please enter your ciphertext: ')
rotationCharacterSet = input('Please enter the rotation value rot5, rot13 or rot47: ')
characters = list(ciphertext.lower())

base = 0  # The first character in the ascii table used by the selected rotation cipher.
offset = 0  # The amount of characters used in the rotation.

if rotationCharacterSet == 'rot47':
    base = 33  # character '!' decimal value.
    offset = 92  # 92 characters used in the rotation cipher.
elif rotationCharacterSet == 'rot13'and ciphertext.isalpha():
    base = 97
    offset = 26
elif rotationCharacterSet == 'rot5' and ciphertext.isdigit():
    base = 48
    offset = 10
else:
    print('You have entered an incorrect rotation value or your cipher text does not match the chosen rotation cipher...')


def rotation(base, offset):
    for x in range(0, offset):
        for y in characters:
            print(chr(base + (((ord(y)-base) + x) % offset)), end ='')
        print('')

rotation(base, offset)
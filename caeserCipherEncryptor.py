# Caeser Cipher Encryptor
from string import ascii_lowercase as alphabet

test = "xyz"

#1 Make Cipher Dict
#2 Loop over letters
    #2.1  lookup position in cipher 
    #2.2  get letter from ascii_lowercase string
#build string and return 

def caeserCipherEncryptor(string, key):
    keys = [(idx + key) % 26 for idx in range(len(alphabet))]
    cipher_dict = dict(zip(alphabet, keys))
    cipher_text = ""
    for letter in string:
        cipher_text += alphabet[cipher_dict[letter]]
    return cipher_text

print(caeserCipherEncryptor(test, 2))

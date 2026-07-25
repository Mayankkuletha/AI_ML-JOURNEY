# Encryption Decryption Program

import random
import string

#instead of writing handwritten long string we are taking some random string from module string , which will be the mixture of punctuations , digits , string.ascii_letters.
words = " " + string.punctuation + string.digits + string.ascii_letters
words= list(words)
keys = words.copy()
random.shuffle(keys)
print(words)
print(keys)
# two list because agr suffle krenege original wali ko khali to kya khte hai mapping same ho jayegi A---> A he rhega niche example hai.
# index = words.index(pas)
    # ciper_text += words[index]



# Encryption

password = input("Enter the word you want to encrypt")
ciper_text=" "
for pas in password :
    index = words.index(pas)
    ciper_text += keys[index]

print(f"original message is {password}")
print(f"encrypted message is {ciper_text}")


# Dcryption
ciper_text= input("Enter the message you want to decrypt")
plainText = " "
for cip in ciper_text:
    index = keys.index(cip)
    plainText+=words[index]

print(f"CiperText was {ciper_text}")
print(f"Plain Text is {plainText}")
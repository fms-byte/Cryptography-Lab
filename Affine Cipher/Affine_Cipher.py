# Encryption Function
def encryption(plaintext, key1, key2):
    ciphertext = ""
    # This for loop is for the traversing the text.
    for i in range(len(plaintext)):
        char = plaintext[i]
        # This condition is for keeping the "space" same on the cipher text.
        if char == " ":
            ciphertext = ciphertext + char
        # Ascii value of upper case letters start from 65.
        elif char.isupper():
            ciphertext = ciphertext + chr(
                ((((ord(char) - 65) * key1) + key2) % 26) + 65
            )
        # Ascii value of lower case letters start from 97.
        else:
            ciphertext = ciphertext + chr(
                ((((ord(char) - 97) * key1) + key2) % 26) + 97
            )
    return ciphertext


# Decryption Function
def decryption(ciphertext, key1, key2):
    plaintext = ""
    # Finding the multiplicative inverse of key1
    mi = pow(key1, -1, 26)
    # This for loop is for the traverse the text.
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        # This condition is for keeping the "space" same on the plaintext.
        if char == " ":
            plaintext = plaintext + char
        # Ascii value of upper case letters start from 65.
        elif char.isupper():
            plaintext = plaintext + chr(((((ord(char) - 65) - key2) * mi) % 26) + 65)
        # Ascii value of lower case letters start from 97.
        else:
            plaintext = plaintext + chr(((((ord(char) - 97) - key2) * mi) % 26) + 97)
    return plaintext


input = open("./input.txt", "r")
output = open("./output.txt", "w")
plaintext = input.read()
key1 = 19
key2 = 7
ciphertext = encryption(plaintext, key1, key2)
decodedtext = decryption(ciphertext, key1, key2)
output.write("Plaintext: " + plaintext + "\n")
output.write("Ciphertext: " + ciphertext.upper() + "\n")
output.write("Decryption of Ciphertext: " + decodedtext.lower() + "\n")

if plaintext.lower() == decodedtext.lower():
    output.write("Decrypted Ciphertext is matched with the given Plaintext.\n")
    output.write("Hence, Decryption is Successful.\n")

# This line is for the closing the files.
input.close()
output.close()
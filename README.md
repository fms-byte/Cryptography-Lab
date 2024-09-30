# **Topic**: Assignment on Cryptography Algorithms 

## 1. Affine Cipher:

```python
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
```

### Input: 
`this is farhan from eleven batch`
### Output: 
```
Plaintext: this is farhan from eleven batch
Ciphertext: EKDL DL YHSKHU YSNB FIFQFU AHETK
Decryption of Ciphertext: this is farhan from eleven batch
Decrypted Ciphertext is matched with the given Plaintext.
Hence, Decryption is Successful.
```

## 2. Playfair Cipher:

### Encryption:
```python
import numpy

# Initialize the matrix
matrix = numpy.array(
   [
       ["m", "o", "n", "a", "r"],
       ["c", "h", "y", "b", "d"],
       ["e", "f", "g", "i", "k"],
       ["l", "p", "q", "s", "t"],
       ["u", "v", "w", "x", "z"],
   ]
)


# This line is for the transpose the matrix.
result = numpy.transpose(matrix)


# Input PlainText.
plaintext = "This is a test message to check the playfair cipher"
p = plaintext
# This line replace all "j" in the plaintext to "i"
plaintext = plaintext.replace("j", "i")
# Remove all the space in the plaintext.
plaintext = plaintext.replace(" ", "")
# Turn the plaintext to lowercase.
plaintext = plaintext.lower()
# This list is use for store the plaintext pair
plaintextpair = []
ciphertextpair = []


# Apply Rule 1: Creation diagram of the plaintext.
# If both letter are same (or only one letter is left)
# Add on "X" after the first letter.
i = 0
while i < len(plaintext):
   a = plaintext[i]
   b = ""


   # If the letter is the last charater of the plaintext.
   if (i + 1) == len(plaintext):
       b = "x"
   else:
       b = plaintext[i + 1]
       # If the two character is not same then this makes pair.
   if a != b:
       plaintextpair.append(a + b)
       i += 2
   else:
       plaintextpair.append(a + "x")
       i += 1
ciphertext = ""
for pair in plaintextpair:
   applied_rule = True


   # Apply Rule 2.
   # If the letters appear at the same row of the table
   # Replace them with the letters to their immediate right --> respectively
   if applied_rule:
       for row in range(5):
           if pair[0] in matrix[row] and pair[1] in matrix[row]:
               for i in range(5):
                   if matrix[row][i] == pair[0]:
                       j0 = i


               for i in range(5):
                   if matrix[row][i] == pair[1]:
                       j1 = i


               applied_rule = False
               ciphertextpair.append(
                   (matrix[row][(j0 + 1) % 5]) + (matrix[row][(j1 + 1) % 5])
               )
               ciphertext = (
                   ciphertext
                   + (matrix[row][(j0 + 1) % 5])
                   + (matrix[row][(j1 + 1) % 5])
               )
   # Apply rule 3.
   # If the letter appear on the same column of table.
   # Replace them with the letter immediate below respectively
   if applied_rule:
       for row in range(5):
           if pair[0] in result[row] and pair[1] in result[row]:
               for i in range(5):
                   if matrix[i][row] == pair[0]:
                       j0 = i


                   for i in range(5):
                       if matrix[i][row] == pair[1]:
                           j1 = i


                   applied_rule = False
               ciphertextpair.append(
                   (matrix[(j0 + 1) % 5][row]) + (matrix[(j1 + 1) % 5][row])
               )
               ciphertext = (
                   ciphertext
                   + (matrix[(j0 + 1) % 5][row])
                   + (matrix[(j1 + 1) % 5][row])
               )
   # Apply rule 4
   # If the letters are not in the same row or same column
   # replace them with the letters on the same row respectively but at the
   # other pair of the corners of the rectangle define by the orginal pair.
   if applied_rule:
       for row in range(5):
           for col in range(5):
               if matrix[row][col] == pair[0]:
                   x0 = row
                   y0 = col
           for row1 in range(5):
               for col1 in range(5):
                   if matrix[row1][col1] == pair[1]:
                       x1 = row1
                       y1 = col1
       ciphertextpair.append((matrix[x0][y1]) + (matrix[x1][y0]))
       ciphertext = ciphertext + (matrix[x0][y1]) + (matrix[x1][y0])




# Turn CipherText to Uppercase
ciphertext = ciphertext.upper()


print("Given Plaintext : ", p)
print("After converting to lowercase and removing spaces: ", plaintext)
print("Ciphertext: ", ciphertext)
```

### Input: 
`This is a test message to check the playfair cipher`
### Output:
```
Given Plaintext :  This is a test message to check the playfair cipher
After converting to lowercase and removing spaces:  thisisatestmessagetochecktheplayfaircipher
Ciphertext:  PDSXSXRSILLRILXBIFPRHYLETZCFQPNBIOKABEVFKM
```

### Decryption:
```python
import numpy

# Initialize the matrix
matrix = numpy.array(
   [
       ["m", "o", "n", "a", "r"],
       ["c", "h", "y", "b", "d"],
       ["e", "f", "g", "i", "k"],
       ["l", "p", "q", "s", "t"],
       ["u", "v", "w", "x", "z"],
   ]
)
# This line is for the transpose the matrix.
result = numpy.transpose(matrix)


# Given Ciphertext
ciphertext = "PDSXSXRSILLRILXBIFPRHYLETZCFQPNBIOKABEVFKM"
c = ciphertext
# This line replace all "j" in the plaintext to "i"
ciphertext = ciphertext.replace("j", "i")
ciphertext = ciphertext.lower()
# This list is use for store the ciphertext and plaintext pair
ciphertextpair = []
plaintextpair = []


# Apply Rule 1.
# make the pair of two letter.
i = 0
while i < len(ciphertext):
   a = ciphertext[i]
   b = ciphertext[i + 1]


   ciphertextpair.append(a + b)
   i = i + 2
plaintext = ""
for pair in ciphertextpair:
   applied_rule = True


   # Apply Rule 2.
   # If the letters appear at the same row of the table
   # Replace them with the letters to their immediate left respectively
   if applied_rule:
       for row in range(5):
           if pair[0] in matrix[row] and pair[1] in matrix[row]:
               for i in range(5):
                   if matrix[row][i] == pair[0]:
                       j0 = i


               for i in range(5):
                   if matrix[row][i] == pair[1]:
                       j1 = i


               applied_rule = False
               plaintextpair.append(
                   (matrix[row][(j0 - 1) % 5]) + (matrix[row][(j1 - 1) % 5])
               )
               plaintext += (matrix[row][(j0 - 1) % 5]) + (matrix[row][(j1 - 1) % 5])
   # Apply rule 3.
   # If the letter appear on the same column of table.
   # Replace them with the letter immediate upper respectively
   if applied_rule:
       for row in range(5):
           if pair[0] in result[row] and pair[1] in result[row]:
               for i in range(5):
                   if matrix[i][row] == pair[0]:
                       j0 = i


                   for i in range(5):
                       if matrix[i][row] == pair[1]:
                           j1 = i


                   applied_rule = False
               plaintextpair.append(
                   (matrix[(j0 - 1) % 5][row]) + (matrix[(j1 - 1) % 5][row])
               )
               plaintext += (matrix[(j0 - 1) % 5][row]) + (matrix[(j1 - 1) % 5][row])
   # Apply rule 4.
   # If the letters are not in the same row or same column
   # replace them with the letters on the same row respectively but at the
   # other pair of the corners of the rectangle define by the orginal pair.
   if applied_rule:
       for row in range(5):
           for col in range(5):
               if matrix[row][col] == pair[0]:
                   x0 = row
                   y0 = col
           for row1 in range(5):
               for col1 in range(5):
                   if matrix[row1][col1] == pair[1]:
                       x1 = row1
                       y1 = col1
       plaintextpair.append((matrix[x0][y1]) + (matrix[x1][y0]))
       plaintext += (matrix[x0][y1]) + (matrix[x1][y0])


print("Given ciphertext: ", c)
print("Decoded plaintext : ", plaintext)
```

### Input: 
`PDSXSXRSILLRILXBIFPRHYLETZCFQPNBIOKABEVFKM`
### Output:
```
Given ciphertext:  PDSXSXRSILLRILXBIFPRHYLETZCFQPNBIOKABEVFKM
Decoded plaintext :  thisisatestmessagetochecktheplayfaircipher
```

## 3. Keyless Transposition Cipher:
### Encryption:
```python
# A python code for the row column transposition Encryption.
import numpy as np

input = open("./input.txt", "r")
output = open("./output.txt", "w")
dInput = open("./d-input.txt", "w")
plaintext = input.read()
p = plaintext
plaintext = plaintext.lower() and plaintext.replace(" ", "")
ciphertext = ""

col = 5
length = len(plaintext)
reminder = length % col
if reminder == 0:
   row = length // col
else:
   row = length // col + 1


# This is dynamic array for the plaintext.
table = np.array([["z"] * col] * row)


# This part is for the fill the tabel dynamically.
index = 0
for i in range(row):
   for j in range(col):
       if index < len(plaintext):
           table[i][j] = plaintext[index]
           index += 1


#Write the matrix into the file
output.write("Given Plaintext: " + p + "\n")
output.write("Col: " + str(col) + "\n")
output.write("Matrix: \n")
for i in range(row):
   for j in range(col):
       output.write(table[i][j] + " ")
   output.write("\n")


# This part is for the make the ciphertext.
table = np.transpose(table)
for i in range(col):
   for j in range(row):       
       ciphertext += table[i][j]


# Write the ciphertext into the file.
output.write("Encrypted Ciphertext: " + ciphertext + "\n")
dInput.write(ciphertext)

# Close the previously open file.
input.close()
output.close()
```

### Input: 
`Md Farhan Masud Shohag`
### Output:
```
Given Plaintext: Md Farhan Masud Shohag
Col: 5
Matrix: 
M d F a r 
h a n M a 
s u d S h 
o h a g z 
Encrypted Ciphertext: MhsodauhFndaaMSgrahz
```

### Decryption:
```python
# A python code for the row column transposition Encryption.
import numpy as np

input = open("./d-input.txt", "r")
output = open("./d-output.txt", "w")
ciphertext = input.read()
plaintext = ""

col = 5
length = len(ciphertext)
reminder = length % col
if reminder == 0:
   row = length // col
else:
   row = length // col + 1

# This is dynamic array for the plaintext.
table = np.array([["z"] * col] * row)

# This part is for the fill the tabel dynamically.
index = 0
for i in range(col):
   for j in range(row):
       if index < len(ciphertext):
           table[j][i] = ciphertext[index]
           index += 1

output.write("Cipher Text: "+ ciphertext + "\n")
output.write("Col: "+ str(col) + "\n")
output.write("Matrix:\n",)

# This part is for the make the plaintext.
for i in range(row):
   for j in range(col):
       output.write(table[i][j] + " ")
       plaintext += table[i][j]
   output.write("\n")

# Write the plaintext into the file.
output.write("Decrypted Plain Text: "+ plaintext)

# Close the previously open file.
input.close()
output.close()
```

### Input: 
`MhsodauhFndaaMSgrahz`
### Output:
```
Cipher Text: MhsodauhFndaaMSgrahz
Col: 5
Matrix:
M d F a r 
h a n M a 
s u d S h 
o h a g z 
Decrypted Plain Text: MdFarhanMasudShohagz
```

## 4. Keyed Transposition Cipher:
### Encryption:
```python
# A python code for encryption keyed transposition cipher.
import numpy as np

input = open("./input.txt", "r")
output = open("./output.txt", "w")
dInput = open("./d-input.txt", "w")
plaintext = input.read()
ciphertext = ""

# This block size is dynamic you can give any value.
blockSize = 4
value = len(plaintext) % blockSize

# This is used for the adding extra dummy character in the plaintext.
if value != 0:
   for i in range(blockSize - value):
       plaintext += "z"

# This line used for find how many block needed for represent the plaintext.
value = int(len(plaintext) / blockSize)
print("Block Needed: ", value)
# This is key need for transfer the plaintext block.
key = [2, 0, 3, 4, 1]

list = np.array([["z"] * value] * blockSize)
list1 = np.array([["z"] * value] * blockSize)
index = 0

# Represent the plaintext into the matrix so that we can transpose the character .
for i in range(blockSize):
   for j in range(value):
       list[i][j] = plaintext[index]
       index += 1

output.write("Plain Text: " + plaintext + "\n")
output.write("Block Size: " + str(blockSize) + "\n")
output.write("Key: " + str(key) + "\n")
output.write("Input Matrix:\n")

# Print the matrix.
for i in range(blockSize):
   for j in range(value):
       output.write(list[i][j] + " ")
   output.write("\n")

# Perform the transposition.
for i in range(blockSize):
   index = 0
   for j in range(value):
       list1[i][j] = list[i][key[index]]
       ciphertext += list1[i][j]
       index += 1


output.write("Output Matrix:\n")

# Print the matrix.
for i in range(blockSize):
   for j in range(value):
       output.write(list1[i][j] + " ")
   output.write("\n")

print("The required ciphertext is : ", ciphertext)

# Write the ciphertext into the output file.
output.write("Cipher Text: " + ciphertext)
dInput.write(ciphertext)

# Close the previously open file.
input.close()
output.close()
```

### Input: 
`MdFarhanMasudShohag`
### Output:
```
Plain Text: MdFarhanMasudShohagz
Block Size: 4
Key: [2, 0, 3, 4, 1]
Input Matrix:
M d F a r 
h a n M a 
s u d S h 
o h a g z 

Output Matrix:
F M a r d 
n h M a a 
d s S h u 
a o g z h 

Cipher Text: FMardnhMaadsShuaogzh
```

### Decryption:
```python
# A python code for encryption keyed transposition cipher.
import numpy as np

input = open("./d-input.txt", "r")
output = open("./d-output.txt", "w")
ciphertext = input.read()
plaintext = ""

# This block size is dynamic you can give any value.
blockSize = 4

# This line used for find how many block needed for represent the ciphertext.
value = int(len(ciphertext) / blockSize)
print("Block Needed: ", value)
# This is key need for transfer the ciphertext block.
key = [1, 4, 0, 2, 3]

list = np.array([["z"] * value] * blockSize)
list1 = np.array([["z"] * value] * blockSize)
index = 0

# Represent the ciphertext into the matrix so that we can transpose the character .
for i in range(blockSize):
   for j in range(value):
       list[i][j] = ciphertext[index]
       index += 1

output.write("Cipher Text: " + ciphertext + "\n")
output.write("Block Size: " + str(blockSize) + "\n")
output.write("Key: " + str(key) + "\n")
output.write("Input Matrix:\n")

# Print the matrix.
for i in range(blockSize):
   for j in range(value):
       output.write(list[i][j] + " ")
   output.write("\n")

# Perform the transposition.
for i in range(blockSize):
   index = 0
   for j in range(value):
       list1[i][j] = list[i][key[index]]
       plaintext += list1[i][j]
       index += 1

output.write("Output Matrix:\n")

# Print the matrix.
for i in range(blockSize):
   for j in range(value):
       output.write(list1[i][j] + " ")
   output.write("\n")

print("The Decoded Plaintext is : ", plaintext)

# Write the plaintext into the output file.
output.write("\nDecoded Plaintext: ")
output.write(plaintext)

# Close the previously open file.
input.close()
output.close()
```

### Input: 
`FMardnhMaadsShuaogzh`
### Output:
```
Cipher Text: FMardnhMaadsShuaogzh
Block Size: 4
Key: [1, 4, 0, 2, 3]
Input Matrix:
F M a r d 
n h M a a 
d s S h u 
a o g z h 

Output Matrix:
M d F a r 
h a n M a 
s u d S h 
o h a g z 

Decoded Plaintext: MdFarhanMasudShohagz
``` 

## 5. AES:
### Encryption:
```python
# A python code for encryption by using AES.
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define the plaintext
plaintext = b'This is a secret message generated by Farhan'
# Generate a 128-bit key
key = get_random_bytes(16)
# Create an AES cipher object in EAX mode (authenticated encryption)
cipher = AES.new(key, AES.MODE_EAX)
# Encrypt the plaintext and get the ciphertext and authentication tag
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Print the encrypted ciphertext and tag
print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Ciphertext :",base64.b64encode(ciphertext))
print("Tag:", tag)

### Input: This is a secret message generated by Farhan
### Output:
Plaintext: b'This is a secret message generated by Farhan'
Key: b'9 \xa0\x1c>nL\xc1\xfc\r\xeb\xb0\x92r\x8b\x88'
Ciphertext: b'@\x07\xd9\r\xd7E\xa9\x03|\xf3\x8d\xa6N$\x08\x85\x93\x86\xdd\xb1\x81y\xea(\xc3\xdc,X,O\xe4\x99\xaa\x9c\xa8\xf1`\xc9^\x08/\x1f0\x02'
Ciphertext : b'QAfZDddFqQN8842mTiQIhZOG3bGBeeoow9wsWCxP5JmqnKjxYMleCC8fMAI='
Tag: b'W\x87v\xb1?\xe9\x81\x9bn\xa1\x9c\x04;l\x01s'

### Decryption:
# Create a new AES cipher object with the same key
# The nonce (number used once) is a crucial component in symmetric key encryption algorithms, particularly in modes like AES.MODE_EAX.
# It serves as an additional input to the encryption algorithm and helps ensure the uniqueness and security of the ciphertext produced.
decrypt_cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)

# Decrypt the ciphertext
decrypted_plaintext = decrypt_cipher.decrypt_and_verify(ciphertext, tag)

# Print the decrypted plaintext
print("Decrypted plaintext:", decrypted_plaintext.decode())
```

### Input: 
```Ciphertext: b'f\xffd\xf4\x02\xcc\x93o\x95Z\x82-_\xc47\x8c\xc2\xee!\x1ax\xd8U\x15xd\xe1\xb4c\x88\xc5\xbf.\xc6\xf7\x96\x0fZN\xe3\xa1:\x02\xaf'```
### Output:
```Decrypted plaintext: This is a secret message generated by Farhan```

## 6. Ceasar Cipher:
```python
#Encryption Function
def encrypt(plaintext,key):
   plaintext = plaintext.upper()
   plaintext = plaintext.replace(" ", "")
   ciphertext = ""
   for i in range(len(plaintext)):
       char = plaintext[i]
       if char == ' ':
           shifted_char = char
       else:
           shifted_char = chr((ord(char) - 65 + key) % 26)
           shifted_char = chr(ord(shifted_char) + 65)
       ciphertext = ciphertext + shifted_char
   return ciphertext

#Decryption Function
def decrypt(ciphertext,key):
   ciphertext = ciphertext.lower()
   decrypted_text = ""
   for i in range(len(ciphertext)):
       char = ciphertext[i]
       if char == ' ':
           shifted_char = char
       else:
           shifted_char = chr((ord(char) - 97 - key) % 26)
           shifted_char = chr(ord(shifted_char) + 97)
       decrypted_text = decrypted_text + shifted_char
   return decrypted_text

#Input
plaintext = "Md Farhan Masud Shohag"
print("Plaintext = " + plaintext)
key = 10
print("Key = " + str(key))
#Output
ciphertext = encrypt(plaintext, key)
print("Ciphertext = " + ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text = " + decrypted_text)
```

### Input: 
```Md Farhan Masud Shohag```
### Output:
```
Plaintext = Md Farhan Masud Shohag
Key = 10
Ciphertext = WNPKBRKXWKCENCRYRKQ
Decrypted text = mdfarhanmasudshohag
```

## 7. DES:
```python
#A python code for encryption by using the data encryption standard
#Import the DES function from Crypto module
import base64
from Crypto.Cipher import DES

#This is the key for encryption
key = 'farhan43'

# This function is for the adding extra text to the plaintext if it does not fill the block
# The block size is 64bit
def pad(text):
   # DES Algorithm works with 8 byte thats why we divided it by 8.
   # If the length of given text is multiple of 8 then exit form the while loop.
   while len(text) % 8 != 0:
       text = text + ' '
   return text
 # Create the object of the DES and pass the appropriate parameter.
# Second parameter is the encryption mode . Several encryption mode are available.
# 'utf-8' encode the string to bytes.As DES require the byte as parameter.
des = DES.new(key.encode('utf-8'),DES.MODE_ECB)

text = 'Md Farhan Masud Shohag'
padded_text = pad(text)

# This encryption function is uesed to encrypt the message.
encrypted_text = des.encrypt(padded_text.encode('utf-8'))

print("The Plaintext is: ", text)
print("The Encrypted Ciphertext is :",encrypted_text)
print("The Encrypted Ciphertext in character format :",base64.b64encode(encrypted_text))

# This decrypt function is used to decrypt the encrypted message.
decrypted_text = des.decrypt(encrypted_text)

print("The Decrypted Ciphertext is :",decrypted_text.decode())
```

### Input: 
```Md Farhan Masud Shohag```
### Key: 
```farhan43```
### Output:
```
The Plaintext is:  Md Farhan Masud Shohag
The Encrypted Ciphertext is : b'r\xe3\x044\x12\xc6\x85<\xc6\xbb\x7f\x8e\xb4m\x1ev-X[\xfc\x9aK\x01\xd8'
The Encrypted Ciphertext in character format : b'cuMENBLGhTzGu3+OtG0edi1YW/yaSwHY'
The Decrypted Ciphertext is : Md Farhan Masud Shohag
```  

## 8. Multiplicative Cipher:
```python
# Input
plaintext = "Md Farhan Masud Shohag"
key = 11


# Encryption Funtion
plaintext = plaintext.upper()
ciphertext = ""
for i in range(len(plaintext)):
   ch = plaintext[i]
   if ch == " ":
       substituted_ch = ch
   else:
       substituted_ch = chr(((ord(ch) - 65) * key) % 26)
       substituted_ch = chr(ord(substituted_ch) + 65)
   ciphertext = ciphertext + substituted_ch
print("Encoded text: ", ciphertext)


# Finding the multiplicative inverse of key value
# Using Extended Euclidean Algorithm
r1 = 26
r2 = key
t1 = 0
t2 = 1
while r2 > 0:
   q = r1 // r2
   r = r1 - q * r2
   r1 = r2
   r2 = r
   t = t1 - q * t2
   t1 = t2
   t2 = t


if r1 == 1:
   ciphertext = ciphertext.lower()
   new_plaintext = ""
   for i in range(len(ciphertext)):
       ch = ciphertext[i]
       if ch == " ":
           substituted_ch = ch
       else:
           substituted_ch = chr(((ord(ch) - 97) * t1) % 26)
           substituted_ch = chr(ord(substituted_ch) + 97)
       new_plaintext = new_plaintext + substituted_ch
   print("Decoded text: ", new_plaintext)


else:
   print("Multiplicative inverse of the key doesn't exist")
```

### Input: 
```Md Farhan Masud Shohag```
### Key: 
```11```
### Output:
```
Encoded text:  CH DAFZAN CAQMH QZYZAO
Decoded text:  md farhan masud shohag
```

## 9. Substitution Cipher:
```python
plaintext1 = "Md Farhan Masud Shohag"
plaintext1 = plaintext1.upper()
ciphertext = ""
key = 19
for i in range(len(plaintext1)):
   ch = plaintext1[i]
   substituted_ch = chr((ord(ch)-65+key) % 26)
   substituted_ch = chr(ord(substituted_ch) + 65)
   ciphertext = ciphertext + substituted_ch
print("Encoded text: ", ciphertext)
ciphertext = ciphertext.lower()
new_plaintext = ""
for i in range(len(ciphertext)):
   ch = ciphertext[i]
   substituted_ch = chr((ord(ch)-97-key) % 26)
   substituted_ch = chr(ord(substituted_ch) + 97)
   new_plaintext = new_plaintext + substituted_ch
print("Decoded text: ", new_plaintext)
```

### Input: 
```Md Farhan Masud Shohag```
### Output: 
```
Encoded text:  FWMYTKATGMFTLNWMLAHATZ
Decoded text:  mdtfarhantmasudtshohag
```

## 10. Vigenere Cipher:
```python
# This function generates the key in a cyclic manner
# until it's length isn't equal to the length of original text
def generateKey(string, key):
   new_key = key
   if len(string) == len(key):
       return key
   else:
       extra_len = len(string) - len(key)
       for i in range(extra_len):
           new_key = new_key + key[i % len(key)]
   return new_key

# Encryption Function
def cipherText(string, key):
   string = string.upper()
   key = key.upper()
   cipher_text = ""
   for i in range(len(string)):
       char = string[i]
       keychar = key[i]
       new_value = chr((((ord(char) - 65) + (ord(keychar) - 65)) % 26) + 65)
       cipher_text = cipher_text + new_value
   return cipher_text

# This function decrypts the encrypted text and returns the original text
def originalText(cipher_text, key):
   cipher_text = cipher_text.lower()
   key = key.lower()
   plaintext = ""
   for i in range(len(cipher_text)):
       char = cipher_text[i]
       keychar = key[i]
       new_value = chr((((ord(char) - 97) - (ord(keychar) - 97)) % 26) + 97)
       plaintext = plaintext + new_value
   return plaintext


# Driver code
if __name__ == "__main__":
   string = "MdFarhanMasudShohag"
   keyword = "idFourtyThree"
   key = generateKey(string, keyword)
   cipher_text = cipherText(string, key)
   plaintext = originalText(cipher_text, key)
   print("Plaintext :", string)
   print("Ciphertext :", cipher_text)
   print("Original/Decrypted Text :", plaintext)

```

### Input: 
```Md Farhan Masud Shohag```
### Key: 
```B190305043```
### Output: 
```
Plaintext : MdFarhanMasudShohag
Ciphertext : UGKOLYTLFHJYHAKTVUX
Original/Decrypted Text : mdfarhanmasudshohag
```

## 11. RSA:
```python
#A Python Code for Encryption Using RSA Algorithm
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#Function for generating public and private key
def generate_key_pair():
   key = RSA.generate(2048)
   public_key = key.publickey().export_key()
   private_key = key.export_key()
   return public_key, private_key

#Encryption Function
def encrypt(message, public_key):
   cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
   encrypted_message = cipher.encrypt(message)
   return encrypted_message

#Decryption Function
def decrypt(encrypted_message, private_key):
   cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
   decrypted_message = cipher.decrypt(encrypted_message)
   return decrypted_message

# Main
plaintext = b"This is a secret message from Md Farhan Masud Shohag"
print("Plaintext:", plaintext)
# Generate key pair
public_key, private_key = generate_key_pair()
# Encrypt the message
encrypted_message = encrypt(plaintext, public_key)
print("Encrypted message:", encrypted_message.hex())
# Decrypt the message
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message.decode())
```

### Input: 
```This is a secret message from Md Farhan Masud Shohag```
### Output: 
```
Plaintext: b'This is a secret message from Md Farhan Masud Shohag'
Encrypted message: 1a490cfc988e771992896058910d907ad7fbce82c2aec095f1de55caeda7a14030c23a43c3c7589f45f6a436d57d3453ec79a5817bb01521896669dc30cabe56d0e3563c78beafb909a3335113831292a846bc5da4b9ea0218ac7a6dbecc3b682493c4780cb06115e255f6500fbf68eeacbe9c53a4297d2d49b0e0f04121c67b4fa014f82e1078d324d0058eae50fd65434710912b3958879e92c0786adca200e5afa1c2c8182ce8b1fc3a6b24c1d71ec373b22e5d657af11653ab3c5267c54b347b65b592fdd4e3a0371a5e7b3fc12ce0c7708597e3fd57efeba99d39153dc87443a76de96190c64ab0e2ca9fdcbda16e84510e177264f5cd1be2dd0a784605
Decrypted message: This is a secret message from Md Farhan Masud Shohag
```

## 12. ElGamal:
```python
# Sympy is a Python library for symbolic mathematics.
from sympy import primitive_root,randprime
import random

# The number for which you want to find the primitive root
prime = randprime(124,10**3)
root = primitive_root(prime)

d=random.randint(1,(prime-2)) # It is private key.

e=(pow(root,d)%prime)  # It is public key.
r=random.randint(1,10)  # Select a random integer.

#Define the plaintext.
plaintext = "This is a secret message from Md Farhan Masud Shohag"
print("Given Plaintext: ", plaintext)

# Encryption Algorithm.
ciphertext=[]
for char in plaintext:
 ciphertext1=(pow(root,r)%prime)
 ciphertext2=((ord(char)*pow(e,r))%prime)
 ciphertext.append((ciphertext1,ciphertext2))
print("Ciphertext: ", ciphertext)

#Decryption Algorithm
plaintext=""
for pair in ciphertext:
 ciphertext1,ciphertext2=pair
 value=pow(ciphertext1,d)
 multinv = pow(value,-1,prime)
 decrypt_char = (ciphertext2*multinv) % prime
 plaintext += chr(decrypt_char)
print("Decrypted Plaintext: ", plaintext)
```

### Input: 
```This is a secret message from Md Farhan Masud Shohag```
### Output:
```
Given Plaintext:  This is a secret message from Md Farhan Masud Shohag
Ciphertext:  [(128, 274), (128, 239), (128, 132), (128, 325), (128, 365), (128, 132), (128, 325), (128, 365), (128, 146), (128, 365), (128, 325), (128, 139), (128, 353), (128, 11), (128, 139), (128, 218), (128, 365), (128, 125), (128, 139), (128, 325), (128, 325), (128, 146), (128, 346), (128, 139), (128, 365), (128, 32), (128, 11), (128, 332), (128, 125), (128, 365), (128, 181), (128, 246), (128, 365), (128, 88), (128, 146), (128, 11), (128, 239), (128, 146), (128, 18), (128, 365), (128, 181), (128, 146), (128, 325), (128, 111), (128, 246), (128, 365), (128, 381), (128, 239), (128, 332), (128, 239), (128, 146), (128, 346)]
Decrypted Plaintext:  This is a secret message from Md Farhan Masud Shohag
```
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
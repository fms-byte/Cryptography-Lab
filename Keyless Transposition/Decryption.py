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

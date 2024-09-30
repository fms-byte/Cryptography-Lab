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

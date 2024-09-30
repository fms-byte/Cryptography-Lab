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

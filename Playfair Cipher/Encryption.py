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

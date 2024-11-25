def generate_playfair_key(keyword):
    """Generates a 5x5 Playfair cipher key matrix from the keyword."""
    alphabet = "abcdefghiklmnopqrstuvwxyz"  # 'j' is excluded
    key = ""
    for char in keyword.lower():
        if char not in key and char in alphabet:
            key += char
    for char in alphabet:
        if char not in key:
            key += char

    # Create a 5x5 matrix
    return [key[i:i+5] for i in range(0, 25, 5)]


def prepare_text(text):
    """Prepares the text for encryption/decryption by pairing letters."""
    text = text.lower().replace(" ", "").replace("j", "i")
    pairs = []
    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text) and text[i] != text[i + 1]:
            char2 = text[i + 1]
            i += 2
        else:
            char2 = 'x'  # Add padding if necessary
            i += 1
        pairs.append((char1, char2))
    return pairs


def find_position(char, key_matrix):
    """Finds the row and column of a character in the key matrix."""
    for row_idx, row in enumerate(key_matrix):
        if char in row:
            return row_idx, row.index(char)
    return None


def playfair_encrypt(text, key_matrix):
    """Encrypts the given text using the Playfair cipher."""
    pairs = prepare_text(text)
    encrypted_text = ""

    for char1, char2 in pairs:
        row1, col1 = find_position(char1, key_matrix)
        row2, col2 = find_position(char2, key_matrix)

        if row1 == row2:  # Same row
            encrypted_text += key_matrix[row1][(col1 + 1) % 5]
            encrypted_text += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += key_matrix[(row1 + 1) % 5][col1]
            encrypted_text += key_matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle swap
            encrypted_text += key_matrix[row1][col2]
            encrypted_text += key_matrix[row2][col1]

    return encrypted_text


def playfair_decrypt(text, key_matrix):
    """Decrypts the given text using the Playfair cipher."""
    pairs = prepare_text(text)
    decrypted_text = ""

    for char1, char2 in pairs:
        row1, col1 = find_position(char1, key_matrix)
        row2, col2 = find_position(char2, key_matrix)

        if row1 == row2:  # Same row
            decrypted_text += key_matrix[row1][(col1 - 1) % 5]
            decrypted_text += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_text += key_matrix[(row1 - 1) % 5][col1]
            decrypted_text += key_matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle swap
            decrypted_text += key_matrix[row1][col2]
            decrypted_text += key_matrix[row2][col1]

    return decrypted_text


# Input and Encryption/Decryption
keyword = "playfair"
key_matrix = generate_playfair_key(keyword)
plain_text = "hello world"

encrypted_text = playfair_encrypt(plain_text, key_matrix)
decrypted_text = playfair_decrypt(encrypted_text, key_matrix)

# Display Results
print("Keyword:", keyword)
print("Key Matrix:")
for row in key_matrix:
    print(row)
print("\nOriginal Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

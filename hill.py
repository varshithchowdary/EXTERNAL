import numpy as np

def mod_inverse(a, m):
    """Calculates the modular inverse of a under modulus m."""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def hill_encrypt(text, key):
    """Encrypts the given text using the Hill cipher with the provided key matrix."""
    text = text.lower().replace(" ", "")  # Convert text to lowercase and remove spaces
    while len(text) % 2 != 0:  # Pad with 'x' if length is not even
        text += 'x'

    text_matrix = np.array([[ord(char) - 97 for char in text[i:i+2]] for i in range(0, len(text), 2)])
    key_matrix = np.array(key)

    encrypted_matrix = (text_matrix @ key_matrix) % 26  # Perform matrix multiplication mod 26
    encrypted_text = ''.join(chr(num + 97) for row in encrypted_matrix for num in row)

    return encrypted_text

def hill_decrypt(ciphertext, key):
    """Decrypts the ciphertext using the Hill cipher with the provided key matrix."""
    key_matrix = np.array(key)
    determinant = int(np.round(np.linalg.det(key_matrix)))  # Calculate determinant
    determinant_mod_inverse = mod_inverse(determinant % 26, 26)  # Modular inverse of determinant

    if determinant_mod_inverse is None:
        raise ValueError("Key matrix is not invertible under mod 26.")

    adjugate = np.linalg.inv(key_matrix).T * determinant  # Adjugate matrix
    inverse_key_matrix = (determinant_mod_inverse * adjugate) % 26  # Modulo 26 inverse matrix
    inverse_key_matrix = inverse_key_matrix.astype(int)

    text_matrix = np.array([[ord(char) - 97 for char in ciphertext[i:i+2]] for i in range(0, len(ciphertext), 2)])
    decrypted_matrix = (text_matrix @ inverse_key_matrix) % 26  # Perform matrix multiplication mod 26
    decrypted_text = ''.join(chr(num + 97) for row in decrypted_matrix for num in row)

    return decrypted_text

# Define a 2x2 key matrix
key_matrix = [[3, 3],
              [2, 5]]

# Input text
plain_text = "help"

# Perform encryption
encrypted_text = hill_encrypt(plain_text, key_matrix)

# Perform decryption
decrypted_text = hill_decrypt(encrypted_text, key_matrix)

# Display results
print("Original Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

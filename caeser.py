def caesar_cipher_encrypt(text, shift):
    """Encrypts the given text using Caesar cipher."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    """Decrypts the given text encrypted with Caesar cipher."""
    return caesar_cipher_encrypt(text, -shift)


# Input text and shift
plain_text = "Hello, World!"
shift_value = 3

# Perform encryption
encrypted_text = caesar_cipher_encrypt(plain_text, shift_value)

# Perform decryption
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value)

# Display results
print("Original Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

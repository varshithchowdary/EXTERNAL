import string

def generate_substitution_key():
    """Generates a random substitution key."""
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet.copy()
    import random
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

def substitution_encrypt(text, key):
    """Encrypts the given text using a substitution cipher."""
    encrypted_text = ""
    for char in text:
        if char.islower():
            encrypted_text += key[char]
        elif char.isupper():
            encrypted_text += key[char.lower()].upper()
        else:
            encrypted_text += char
    return encrypted_text

def substitution_decrypt(text, key):
    """Decrypts the given text using a substitution cipher."""
    reverse_key = {v: k for k, v in key.items()}
    decrypted_text = ""
    for char in text:
        if char.islower():
            decrypted_text += reverse_key[char]
        elif char.isupper():
            decrypted_text += reverse_key[char.lower()].upper()
        else:
            decrypted_text += char
    return decrypted_text

# Generate a substitution key
substitution_key = generate_substitution_key()

# Input text
plain_text = "Hello, World!"

# Perform encryption
encrypted_text = substitution_encrypt(plain_text, substitution_key)

# Perform decryption
decrypted_text = substitution_decrypt(encrypted_text, substitution_key)

# Display results
print("Original Text:", plain_text)
print("Substitution Key:", substitution_key)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

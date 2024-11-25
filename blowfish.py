from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

def blowfish_encrypt(key, plaintext):
    """
    Encrypts plaintext using the Blowfish algorithm.
    :param key: Secret key (4 to 56 bytes long)
    :param plaintext: Text to encrypt
    :return: Encrypted ciphertext
    """
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)  # Create Blowfish cipher in ECB mode
    padded_text = pad(plaintext.encode(), Blowfish.block_size)  # Pad plaintext to match block size
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def blowfish_decrypt(key, ciphertext):
    """
    Decrypts ciphertext using the Blowfish algorithm.
    :param key: Secret key (4 to 56 bytes long)
    :param ciphertext: Encrypted text
    :return: Decrypted plaintext
    """
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)  # Create Blowfish cipher in ECB mode
    decrypted_text = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)  # Remove padding
    return decrypted_text.decode()

# Example Usage
key = b'SecretKey'  # Key must be 4 to 56 bytes long
plaintext = "Hello, World!"  # Text to encrypt

# Encrypt the plaintext
ciphertext = blowfish_encrypt(key, plaintext)
print("Encrypted Text:", ciphertext.hex())

# Decrypt the ciphertext
decrypted_text = blowfish_decrypt(key, ciphertext)
print("Decrypted Text:", decrypted_text)

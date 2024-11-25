from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(key, plaintext):
    """
    Encrypts plaintext using DES algorithm.
    :param key: 8-byte key
    :param plaintext: Text to encrypt
    :return: Encrypted ciphertext
    """
    des = DES.new(key, DES.MODE_ECB)  # Create DES cipher in ECB mode
    padded_text = pad(plaintext.encode(), DES.block_size)  # Pad the plaintext to make it a multiple of the block size
    ciphertext = des.encrypt(padded_text)
    return ciphertext

def des_decrypt(key, ciphertext):
    """
    Decrypts ciphertext using DES algorithm.
    :param key: 8-byte key
    :param ciphertext: Encrypted text
    :return: Decrypted plaintext
    """
    des = DES.new(key, DES.MODE_ECB)  # Create DES cipher in ECB mode
    decrypted_text = unpad(des.decrypt(ciphertext), DES.block_size)  # Remove padding after decryption
    return decrypted_text.decode()

# Example Usage
key = b'8bytekey'  # Key must be exactly 8 bytes
plaintext = "Hello, World!"  # Text to encrypt

# Encrypt the plaintext
ciphertext = des_encrypt(key, plaintext)
print("Encrypted Text:", ciphertext.hex())

# Decrypt the ciphertext
decrypted_text = des_decrypt(key, ciphertext)
print("Decrypted Text:", decrypted_text)

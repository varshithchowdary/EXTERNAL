from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def rijndael_encrypt(key, plaintext):
    """
    Encrypts plaintext using the Rijndael (AES) algorithm.
    :param key: Secret key (16, 24, or 32 bytes for AES-128, AES-192, or AES-256)
    :param plaintext: Text to encrypt
    :return: Encrypted ciphertext
    """
    cipher = AES.new(key, AES.MODE_ECB)  # Create AES cipher in ECB mode
    padded_text = pad(plaintext.encode(), AES.block_size)  # Pad plaintext to match block size
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def rijndael_decrypt(key, ciphertext):
    """
    Decrypts ciphertext using the Rijndael (AES) algorithm.
    :param key: Secret key (16, 24, or 32 bytes for AES-128, AES-192, or AES-256)
    :param ciphertext: Encrypted text
    :return: Decrypted plaintext
    """
    cipher = AES.new(key, AES.MODE_ECB)  # Create AES cipher in ECB mode
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Remove padding
    return decrypted_text.decode()

# Example Usage
key = b'SixteenByteKey!'
  # Key must be 16, 24, or 32 bytes
plaintext = "Hello, Rijndael!"  # Text to encrypt

# Encrypt the plaintext
ciphertext = rijndael_encrypt(key, plaintext)
print("Encrypted Text:", ciphertext.hex())

# Decrypt the ciphertext
decrypted_text = rijndael_decrypt(key, ciphertext)
print("Decrypted Text:", decrypted_text)

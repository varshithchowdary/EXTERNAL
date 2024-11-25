from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

def generate_rsa_keys():
    """
    Generates RSA public and private keys.
    :return: A tuple of (private_key, public_key)
    """
    key = RSA.generate(2048)  # Generate a 2048-bit RSA key pair
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def rsa_encrypt(public_key, plaintext):
    """
    Encrypts plaintext using the RSA algorithm.
    :param public_key: RSA public key
    :param plaintext: Text to encrypt
    :return: Encrypted ciphertext
    """
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

def rsa_decrypt(private_key, ciphertext):
    """
    Decrypts ciphertext using the RSA algorithm.
    :param private_key: RSA private key
    :param ciphertext: Encrypted text
    :return: Decrypted plaintext
    """
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text.decode()

# Example Usage
private_key, public_key = generate_rsa_keys()
print("Private Key:\n", private_key.decode())
print("Public Key:\n", public_key.decode())

plaintext = "Hello, RSA!"
print("\nOriginal Text:", plaintext)

# Encrypt the plaintext
ciphertext = rsa_encrypt(public_key, plaintext)
print("\nEncrypted Text (Hex):", ciphertext.hex())

# Decrypt the ciphertext
decrypted_text = rsa_decrypt(private_key, ciphertext)
print("\nDecrypted Text:", decrypted_text)

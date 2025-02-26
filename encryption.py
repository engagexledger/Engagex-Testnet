from Crypto.Cipher import AES
import base64

KEY = b'Sixteen byte key'

def encrypt_data(data):
    cipher = AES.new(KEY, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    return base64.b64encode(nonce + ciphertext).decode()

def decrypt_data(encrypted_data):
    raw_data = base64.b64decode(encrypted_data)
    nonce = raw_data[:16]
    ciphertext = raw_data[16:]
    cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()

if __name__ == "__main__":
    test_data = "Hello, EngageX!"
    encrypted = encrypt_data(test_data)
    decrypted = decrypt_data(encrypted)

    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

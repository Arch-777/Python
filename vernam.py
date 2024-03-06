import random

def encrypt_decrypt(text, key):
   return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(text, key))

def generate_key(length):
   return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

if __name__ == "__main__":
   plaintext = "HELLO"
   key = generate_key(len(plaintext))

   print("Plaintext:", plaintext)
   print("Key:", key)

   ciphertext = encrypt_decrypt(plaintext, key)
   print("Ciphertext:", ciphertext)

   decrypted_text = encrypt_decrypt(ciphertext, key)  # Same operation for both encryption and decryption
   print("Decrypted Text:", decrypted_text)

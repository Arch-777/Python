def rail_fence(message, rails):
  """
  Encrypts or decrypts a message using the Rail Fence technique.

  Args:
      message: The message to encrypt or decrypt.
      rails: The number of rails to use.

  Returns:
      The encrypted or decrypted message.
  """
  fence = ["" for _ in range(rails)]  # Create empty rails
  row, dir = 0, False  # Initialize variables

  for char in message:
    fence[row] += char
    row += 1 if not dir else -1
    dir = not dir if (row == 0 or row == rails - 1) else dir

  # Combine characters from rails for output
  cipher = "".join(fence)
  return cipher

# Example usage
message = "Hello, World!"
rails = 3  # Number of rails

encrypted_message = rail_fence(message, rails)
decrypted_message = rail_fence(encrypted_message, rails)  # Use same function for decryption

print("Original Message:", message)
print("Encrypted Message (", rails, " rails):", encrypted_message)
print("Decrypted Message:", decrypted_message)



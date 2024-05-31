def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        # Check if the character is printable and has a corresponding Unicode code point
        if ord(char) >= 32 and ord(char) <= 126:  # ASCII printable characters
            # Calculate the new Unicode code point after shifting
            new_code_point = (ord(char) - 32 + shift) % 95 + 32
            encrypted_text += chr(new_code_point)
        else:
            # If the character is not printable or doesn't have a corresponding Unicode code point, leave it unchanged
            encrypted_text += char
    return encrypted_text

def main():
    choice: "What would you like to do? For text Encryption, press "e". For text Decryption, press "d".
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (an integer): "))
    if choice = = "e": 
      encrypted_message = caesar_cipher(text, shift)
      print("Encrypted message:", encrypted_message)
if choice = = "d": 
      decrypted_message = caesar_cipher(text, -shift)
      print("Decrypted message:", decrypted_message)


if __name__ == "__main__":
    main()

def caesar_encrypt(text, shift):
    encrypted_message = ""
    for char in text:
        if char.isalpha():
            # Shift within alphabet bounds
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_message += encrypted_char
        else:
            # Non-alphabetical characters unchanged
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(text, shift):
    # Decrypt by shifting in the opposite direction
    return caesar_encrypt(text, -shift)

def main():
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))

    encrypted = caesar_encrypt(message, shift)
    print(f"Encrypted message: {encrypted}")

    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("You want to encrypt or decrypt message? (e/d): ").lower()
        if choice not in ('e', 'd'):
            print("Invalid choice... Please enter 'e' for encrypt or 'd' for decrypt")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
        if choice == 'e':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'd':
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
        
        another = input("Would you like to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()


    
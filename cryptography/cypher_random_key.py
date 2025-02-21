import secrets
import string

# Define the alphabet
alphabet = string.ascii_letters + string.digits + string.punctuation

# Function to generate a random decryption key
def generate_decryption_key(length=16): 
    key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return key

# Generate a random decryption key and print it
decryption_key = generate_decryption_key(16)
print(f"🔑 Random Decryption Key: {decryption_key}")

# Custom cipher function for encryption and decryption
def custom_cypher(message, key, encrypt=True):
    new_alphabet = key + ''.join([char for char in alphabet if char not in key])

    result = ''

    for char in message:
        if char in alphabet:
            if encrypt:
                result += new_alphabet[alphabet.index(char) % len(new_alphabet)]
            else:
                result += alphabet[new_alphabet.index(char) % len(alphabet)]
        else:
            result += char

    return result

# Main function to handle user input
def main():
    user_choice = input('💬 Do you want to encrypt or decrypt a message? (e/d) q to quit: ')
    while user_choice != 'q':
        if user_choice == 'e':
            user_message = input('🔒 Enter a message to encrypt: ')
            encrypted_message = custom_cypher(user_message, decryption_key, True)
            print(f"🔐 Encrypted message: {encrypted_message}")
        elif user_choice == 'd':
            user_message = input('🔑 Enter a message to decrypt: ')
            user_key = input('🔑 Enter the decryption key: ')
            decrypted_message = custom_cypher(user_message, user_key, False)
            print(f"🔓 Decrypted message: {decrypted_message}")
        else:
            print('❌ Invalid choice. Please enter e or d.')

        user_choice = input('💬 Do you want to encrypt or decrypt a message? (e/d) q to quit: ')

# Run the program
if __name__ == '__main__':
    main()

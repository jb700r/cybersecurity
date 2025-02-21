import hashlib
from itertools import product

lower_case = [chr(i) for i in range(ord('a'), ord('z') + 1)]
upper_case = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
numbers = [str(i) for i in range(0, 10)]
special_characters = list("!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/")

all_chars = lower_case + upper_case + numbers + special_characters

def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def crack(hashed_pw, length):
    for combo in product(all_chars, repeat=length):
        candidate = ''.join(combo)
        print(f"Trying: {candidate}")
        if get_hash(candidate) == hashed_pw:
            print(f"Password is: {candidate}")
            return candidate
    print("Password not found")
    return None

def main():
    user_hashed_pw = input('Enter hashed password (MD5 hex format): ').strip()
    user_length_input = int(input('Enter the length of the password: '))
    
    cracked_pw = crack(user_hashed_pw, user_length_input)
    if cracked_pw:
        print(f"Successfully cracked: {cracked_pw}")
    else:
        print("Failed to crack the password.")

if __name__ == '__main__':
    main()

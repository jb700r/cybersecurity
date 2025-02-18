import hashlib
import string
import multiprocessing
from itertools import product

all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest() 

def generate_combinations(length, start_index, step):
    """Generate password combinations, each worker processing every `step`th combination."""
    for i, combo in enumerate(product(all_chars, repeat=length)):
        if i % step == start_index:  # Ensure unique start positions per worker
            yield ''.join(combo)

def crack_worker(hashed_pw, length, start_index, step):
    """Worker function to check a portion of the password space."""
    for candidate in generate_combinations(length, start_index, step):
        if get_hash(candidate) == hashed_pw:
            print(f"Password found: {candidate}")
            return candidate
    return None

def crack(hashed_pw, length):
    num_workers = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_workers)

    # Assign unique start index to each worker
    results = pool.starmap(crack_worker, [(hashed_pw, length, i, num_workers) for i in range(num_workers)])

    pool.close()
    pool.join()

    for result in results:
        if result:
            return result  # Return as soon as one worker finds the password

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

import hashlib
import string
import multiprocessing
from itertools import product
import time

# Character sets
all_ascii = string.ascii_lowercase + string.ascii_uppercase  # Ensure both cases are included
all_numbers = string.digits
all_special = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"

def get_hash(text):
    """Returns the MD5 hash of a given text."""
    return hashlib.md5(text.encode()).hexdigest()

def generate_combinations(length, start_index, step, charset):
    """Generates possible password combinations."""
    for i, combo in enumerate(product(charset, repeat=length)):
        if i % step == start_index:
            yield ''.join(combo)

def crack_worker(args):
    """Worker function to brute force the password."""
    hashed_pw, length, start_index, step, charset = args
    for candidate in generate_combinations(length, start_index, step, charset):
        if get_hash(candidate) == hashed_pw:
            return candidate
    return None

def crack(hashed_pw, length, charset):
    """Main function to distribute work across multiple processes."""
    num_workers = multiprocessing.cpu_count()  # Use all CPU cores
    print(f"⚡ Cracking password with {num_workers} workers...")

    with multiprocessing.Pool(num_workers) as pool:
        for result in pool.imap_unordered(crack_worker, [(hashed_pw, length, i, num_workers, charset) for i in range(num_workers)]):
            if result:
                pool.terminate()  # Stop other processes
                return result

    print("❌ Password not found")
    return None

def main():
    """User input and execution."""
    # User input
    user_hashed_pw = input('🔑 Enter hashed password (MD5 hex format): ').strip()
    user_length_input = int(input('🔢 Enter the length of the password: '))
    user_input_charset = input('🛠️  Select charset: (1) Letters (2) Numbers (3) Special: ').strip()

    # Build charset
    charset = ""
    if "1" in user_input_charset:
        charset += all_ascii
    if "2" in user_input_charset:
        charset += all_numbers
    if "3" in user_input_charset:
        charset += all_special

    if not charset:
        print("⚠️ Invalid input, no character set selected.")
        return

    print(f"🚀 Cracking password with charset: {charset}")

    # Start cracking
    start = time.time()
    cracked_pw = crack(user_hashed_pw, user_length_input, charset)

    if cracked_pw:
        print(f"✅ Successfully cracked: {cracked_pw}")
    else:
        print("❌ Failed to crack the password.")

    print(f"⏳ Time taken: {time.time() - start:.2f} seconds")

if __name__ == '__main__':
    main()

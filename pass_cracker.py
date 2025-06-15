import itertools
import string
import time

def print_banner():
    banner = """
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║          ██████╗  █████╗  ██████╗ ███████╗         ║
    ║         ██╔════╝ ██╔══██╗██╔════╝ ██╔════╝         ║
    ║        █████╗   ███████║██║  ███╗███████╗         ║
    ║       ██╔══╝   ██╔══██║██║   ██║╚════██║         ║
    ║      ██║      ██║  ██║╚██████╔╝███████║         ║
    ║      ╚═╝      ╚═╝  ╚═╝ ╚═════╝ ╚══════╝         ║
    ║                                                    ║
    ║   PassCracker: A Simple Password Cracking Tool     ║
    ║   Coded by Pakistani Ethical Hacker:               ║
    ║   Mr. Sabaz Ali Khan                               ║
    ║                                                    ║
    ╚════════════════════════════════════════════════════╝
    """
    print(banner)

def brute_force_cracker(target_password, max_length=4, charset=string.ascii_lowercase):
    print(f"[*] Attempting to crack password: {target_password}")
    print(f"[*] Using character set: {charset}")
    print(f"[*] Maximum password length: {max_length}")
    
    start_time = time.time()
    attempts = 0
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target_password:
                end_time = time.time()
                print(f"\n[+] Password found: {guess}")
                print(f"[+] Attempts made: {attempts}")
                print(f"[+] Time taken: {end_time - start_time:.2f} seconds")
                return guess
            if attempts % 1000 == 0:
                print(f"[*] Tried: {guess}, Attempts: {attempts}")
    
    print("\n[-] Password not found.")
    return None

def main():
    print_banner()
    target_password = "test"  # Example password for demonstration
    print("\n[*] Starting PassCracker...")
    print("[*] This is a demo tool for educational purposes only.")
    
    cracked_password = brute_force_cracker(target_password)
    
    if cracked_password:
        print(f"\n[+] Success! The password is: {cracked_password}")
    else:
        print("\n[-] Failed to crack the password.")

if __name__ == "__main__":
    main()
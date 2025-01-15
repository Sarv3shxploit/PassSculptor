import re
from colorama import Fore, Style
import time
import sys
import pyfiglet  # Import pyfiglet for ASCII art text
import random  # Import random for password generation

# Common passwords for detection
COMMON_PASSWORDS = ["12345678", "password", "123456789", "1234567890", "qwertyuiop", 
"asdfghjkl", "password1", "qwerty123", "abc123456", "letmein123", 
"welcome1", "admin123", "iloveyou1", "1234567a", "superman1", 
"sunshine", "princess", "qwertyui", "password123", "lovely123", 
"freedom1", "football", "starwars", "whatever", "nintendo", 
"batman123", "pokemon1", "dragon123", "monkey123", "killer123"
]

def print_animated_text(text, delay=0.001):  # Adjusted delay for faster speed
    """
    Print text with an animation effect by printing one character at a time.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text

def get_password():
    """
    Prompt the user to enter a password.
    """
    password = input("Enter your password to check its strength: ")
    return password

def check_length(password):
    """
    Check if the password length is at least 8 characters.
    """
    return len(password) >= 8

def check_lowercase(password):
    """
    Check if the password contains at least one lowercase letter.
    """
    return bool(re.search(r'[a-z]', password))

def check_uppercase(password):
    """
    Check if the password contains at least one uppercase letter.
    """
    return bool(re.search(r'[A-Z]', password))

def check_digit(password):
    """
    Check if the password contains at least one digit.
    """
    return bool(re.search(r'\d', password))

def check_special_char(password):
    """
    Check if the password contains at least one special character.
    """
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def check_invalid_characters(password):
    """
    Check if the password contains invalid characters such as hyphens or spaces.
    """
    return " " in password or "-" in password

def is_common_password(password):
    """
    Check if the password is part of the common passwords list.
    """
    return password in COMMON_PASSWORDS

def generate_strong_password(length=8, use_special_chars=True, use_digits=True):
    """
    Generate a strong password based on user-defined criteria.
    """
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*()_+"
    
    all_chars = lower + upper
    if use_digits:
        all_chars += digits
    if use_special_chars:
        all_chars += special
    
    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def evaluate_password(password):
    """
    Evaluate the strength of the password based on various criteria.
    Returns a score and list of feedback messages.
    """
    score = 0
    feedback = []

    if check_invalid_characters(password):
        feedback.append(f"{Fore.RED}Password should not contain spaces or hyphens (-).{Style.RESET_ALL}")
        return score, feedback

    if is_common_password(password):
        feedback.append(f"{Fore.RED}Your password is too common and easily guessable.{Style.RESET_ALL}")
        return score, feedback

    if check_length(password):
        score += 1
    else:
        feedback.append(f"{Fore.MAGENTA}Password should be at least 8 characters long.🔒{Style.RESET_ALL}")

    if check_lowercase(password):
        score += 1
    else:
        feedback.append(f"{Fore.MAGENTA}Include at least one lowercase letter. <a-z> {Style.RESET_ALL}")

    if check_uppercase(password):
        score += 1
    else:
        feedback.append(f"{Fore.MAGENTA}Include at least one uppercase letter. <A-Z> {Style.RESET_ALL}")

    if check_digit(password):
        score += 1
    else:
        feedback.append(f"{Fore.MAGENTA}Include at least one digit. <0-9> {Style.RESET_ALL}")

    if check_special_char(password):
        score += 1
    else:
        feedback.append(f"{Fore.MAGENTA}Include at least one special character <e.g., !, @, #, etc.> {Style.RESET_ALL}")

    return score, feedback

def display_results(score, feedback):
    print_animated_text(f"\n{Fore.CYAN}Password Strength Evaluation:{Style.RESET_ALL}")
    print_animated_text(f"{Fore.GREEN if score == 5 else Fore.YELLOW if score >= 3 else Fore.RED}Score: {score}/5{Style.RESET_ALL}")

    if feedback:
        print_animated_text(f"{Fore.YELLOW if score >= 3 else Fore.RED}Recommendations to Improve Your Password:{Style.RESET_ALL}")
        for item in feedback:
            print_animated_text(f"- {item}", delay=0.005)

def password_strength_checker():
    """
    Main function to run the Password Strength Checker.
    """
    # Create a colorful, big text banner using pyfiglet
    banner = pyfiglet.figlet_format("PassSculptor", font="doom", width=80)
    print_animated_text(Fore.GREEN + banner, delay=0.002)

    while True:
        print(f"{Fore.CYAN}\n1. Check Password Strength{Style.RESET_ALL}")
        print(f"{Fore.CYAN}2. Generate a Strong Password{Style.RESET_ALL}")
        print(f"{Fore.CYAN}3. Exit{Style.RESET_ALL}")
        choice = input("Enter your choice: ")

        if choice == "1":
            password = get_password()
            score, feedback = evaluate_password(password)
            display_results(score, feedback)
        elif choice == "2":
            length = int(input("Enter desired password length (default 8): ") or 8)
            use_special_chars = input("Include special characters? (y/n, default y): ").lower() != "n"
            use_digits = input("Include digits? (y/n, default y): ").lower() != "n"
            generated_password = generate_strong_password(length, use_special_chars, use_digits)
            print_animated_text(f"{Fore.GREEN}Generated Password: {generated_password}{Style.RESET_ALL}")
        elif choice == "3":
            print_animated_text(f"{Fore.CYAN}Exiting...{Style.RESET_ALL}")
            break
        else:
            print_animated_text(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    password_strength_checker()

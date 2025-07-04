import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    all_chars = lower + upper + digits + symbols

    if not all_chars:
        raise ValueError("No character sets selected for password generation.")

    password = []
    password.append(random.choice(lower))
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password[:length])

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    length = int(input("Enter password length (minimum 4): "))
    if length < 4:
        print("Password length should be at least 4.")
    else:
        password = generate_password(length)
        print(f"Generated password: {password}")
import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def password_generator(strength):
    if strength == "easy":
        return generate_password(6, include_digits=False, include_special_chars=False)
    elif strength == "medium":
        return generate_password(10, include_digits=True, include_special_chars=False)
    elif strength == "hard":
        return generate_password(14, include_digits=True, include_special_chars=True)
    else:
        return "Invalid strength. Please choose 'easy', 'medium', or 'hard'."

if __name__ == "__main__":
    strength = input("Choose password strength (easy, medium, or hard): ").lower()
    password = password_generator(strength)
    print(f"Generated {strength} password: {password}")

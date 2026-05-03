import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        strength += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1

    # Numbers
    if re.search(r"[0-9]", password):
        strength += 1

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Result
    if strength <= 2:
        return "Weak ❌"
    elif strength == 3 or strength == 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"


# User input
password = input("Enter your password: ")
result = check_password_strength(password)

print("Password Strength:", result)
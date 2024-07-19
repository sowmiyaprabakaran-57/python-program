import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    if not re.search(r"[a-z]", password):
        return "Weak: Password should contain at least one lowercase letter."

    if not re.search(r"[A-Z]", password):
        return "Weak: Password should contain at least one uppercase letter."

    if not re.search(r"[0-9]", password):
        return "Weak: Password should contain at least one digit."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets all criteria."

def main():
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()

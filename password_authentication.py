import re

def check_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters"

    if not re.search("[A-Z]", password):
        return "Password must contain an uppercase letter"

    if not re.search("[a-z]", password):
        return "Password must contain a lowercase letter"

    if not re.search("[0-9]", password):
        return "Password must contain a number"

    if not re.search("[@#$%^&+=]", password):
        return "Password must contain a special character"

    return "Strong Password!"

password = input("Enter your password: ")
print(check_password(password))
import random
import string
import pyperclip  

def generate_password(min_length, numbers=True, special_characters=True, avoid_ambiguous=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    ambiguous_chars = "Il1O0"

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    if avoid_ambiguous:
        characters = ''.join(c for c in characters if c not in ambiguous_chars)

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

def evaluate_password_strength(password):
    length_score = len(password) >= 12
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    strength_score = sum([length_score, has_upper, has_lower, has_number, has_special])
    strength_levels = {1: "Weak", 2: "Moderate", 3: "Strong", 4: "Very Strong", 5: "Excellent"}
    return strength_levels.get(strength_score, "Weak")


min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to include numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to include special characters (y/n)? ").lower() == "y"
avoid_ambiguous = input("Avoid ambiguous characters (e.g., 1, l, O, 0) (y/n)? ").lower() == "y"


pwd = generate_password(min_length, has_number, has_special, avoid_ambiguous)
strength = evaluate_password_strength(pwd)


print("\nGenerated Password:", pwd)
print("Password Strength:", strength)


pyperclip.copy(pwd)
print("\nThe password has been copied to your clipboard!")



        

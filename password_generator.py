import random
import string

def generate_password(length=12, use_special=True):
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter desired password length (e.g. 12): "))
        special = input("Include special characters? (y/n): ").lower() == 'y'
        password = generate_password(length, special)
        print(f"\n🧾 Your generated password:\n{password}")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()

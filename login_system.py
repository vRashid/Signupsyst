import os

USERS_FILE = "users.txt"

# Ensure the users file exists
if not os.path.exists(USERS_FILE):
    open(USERS_FILE, "w").close()

def signup():
    """Registers a new user."""
    email = input("Enter your email: ")
    password = input("Enter your password (min 6 characters): ")

    with open(USERS_FILE, "a") as file:
        file.write(f"{email} {password}\n")

    print("Registration successful!")

def login():
    """Logs in a user."""
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    with open(USERS_FILE, "r") as file:
        users = file.readlines()

    for user in users:
        saved_email, saved_password = user.strip().split()
        if email == saved_email and password == saved_password:
            print(f"Login successful! Welcome, {email}.")
            return

    print("Invalid email or password. Try again.")

def main():
    """Main function to choose between login and signup."""
    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

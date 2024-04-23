def get_password():
    return input("Enter the password: ")

def main():
    password = "correct_password"
    entered_password = get_password()
    
    while entered_password != password:
        print("Incorrect password. Try again.")
        entered_password = get_password()
    
    print("Success! You entered the correct password.")

if __name__ == "__main__":
    main()
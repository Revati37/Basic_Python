def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Initialize pointers for the start and end of the string
    start = 0
    end = len(s) - 1
    
    # Use a while loop to check if the string is a palindrome
    while start < end:
        # If characters at both pointers don't match, it's not a palindrome
        if s[start] != s[end]:
            return False
        # Move pointers towards each other
        start += 1
        end -= 1
    
    return True

def main():
    # Ask the user to enter a string
    string = input("Enter a string: ")
    
    # Check if the string is a palindrome
    if is_palindrome(string):
        print("The given string is a palindrome.")
    else:
        print("The given string is not a palindrome.")

if __name__ == "__main__":
    main()
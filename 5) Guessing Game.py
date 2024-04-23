import random

def main():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    
    # Keep track of the number of guesses
    num_guesses = 0
    
    # Loop until the correct number is guessed
    while True:
        # Ask the user to guess the number
        guess = int(input("Guess the number between 1 and 100: "))
        
        # Increment the number of guesses
        num_guesses += 1
        
        # Check if the guess is correct
        if guess == target_number:
            print("Congratulations! You guessed the correct number in", num_guesses, "guesses.")
            break
        elif guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

if __name__ == "__main__":
    main()
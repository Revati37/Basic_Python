def sum_of_digits(number):
    # Initialize the sum
    digit_sum = 0
    
    # Use a while loop to extract digits and add them to the sum
    while number > 0:
        # Extract the rightmost digit
        digit = number % 10
        # Add the digit to the sum
        digit_sum += digit
        # Remove the rightmost digit from the number
        number //= 10
    
    return digit_sum

def main():
    # Ask the user to enter a number
    number = int(input("Enter a number: "))
    
    # Calculate the sum of digits
    total = sum_of_digits(number)
    
    # Print the sum of digits
    print("The sum of digits of the number is:", total)

if __name__ == "__main__":
    main()
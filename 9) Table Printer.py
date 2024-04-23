def multiplication_table(number):
    # Initialize the counter
    i = 1
    
    # Print the multiplication table using a while loop
    while i <= 10:
        # Calculate the product
        result = number * i
        # Print the result in the format "number x i = result"
        print(number, "x", i, "=", result)
        # Increment the counter
        i += 1

def main():
    # Ask the user to enter a number
    number = int(input("Enter a number to print its multiplication table: "))
    
    # Print the multiplication table of the given number
    print("Multiplication table of", number, ":")
    multiplication_table(number)

if __name__ == "__main__":
    main()
def fibonacci_series(n):
    # Initialize the first two terms of the Fibonacci series
    fibonacci_sequence = [0, 1]
    
    # Use a while loop to generate Fibonacci series up to n terms
    while len(fibonacci_sequence) < n:
        # Calculate the next term by adding the previous two terms
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        # Append the next term to the sequence
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

def main():
    # Ask the user for the number of terms in the Fibonacci series
    num_terms = int(input("Enter the number of terms in the Fibonacci series: "))
    
    # Print the Fibonacci series up to the specified number of terms
    print("Fibonacci series up to", num_terms, "terms:")
    series = fibonacci_series(num_terms)
    for term in series:
        print(term, end=" ")

if __name__ == "__main__":
    main()
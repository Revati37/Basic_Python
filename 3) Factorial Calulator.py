def calculate_factorial(n):
    factorial = 1
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        while n > 0:
            factorial *= n
            n -= 1
        return factorial

# Test the function
number = int(input("Enter a number to calculate its factorial: "))
result = calculate_factorial(number)
print("Factorial of", number, "is", result)
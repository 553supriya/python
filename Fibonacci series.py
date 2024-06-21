def fibonacci(n):
    fib_series = []
    # Initialize the first two terms of the Fibonacci series
    a, b = 0, 1

    # Generate Fibonacci series up to the nth term
    for _ in range(n):
        fib_series.append(a)
        # Calculate the next term by adding the previous two terms
        a, b = b, a + b

    return fib_series


# Input the number of terms for the Fibonacci series
n = int(input("Enter the number of terms for the Fibonacci series: "))

# Print the Fibonacci series
print("Fibonacci series up to", n, "terms:")
print(fibonacci(n))

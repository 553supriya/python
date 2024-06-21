def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input a number from the user
number = int(input("Enter a number: "))

# Check whether the number is even or odd
result = check_even_odd(number)
print(f"The number {number} is {result}.")

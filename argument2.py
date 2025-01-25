def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Please enter a number:"))
if num < 0:
    print("Factorial number doesn't exist in negative numbers." )
else:
    print(f"The factorial of {num} is {factorial (num)}")
def add(P, Q):
    return P+Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def division(P, Q):
    return P / Q
print("Please select the operation:-")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")


choice = input("Please enter a choice (a/b/c/d):")
num1 = int(input("Please enter the first number:"))
num2 = int(input("Please enter the second number:"))
if choice == 'a':
    print(num1, "+", num2, "=", add(num1, num2))
if choice == 'b':
    print(num1, "-", num2, "=", subtract(num1, num2))
if choice == 'c':
    print(num1, "*", num2, "=", multiply(num1, num2))
if choice == 'd':
    print(num1, "/", num2, "=", division(num1, num2))
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

if op == "+":
    result = a + b
    print("The result of addition is: ", result)
elif op == "-":
    result = a - b
    print("The result of subtraction is: ", result)
elif op == "*":
    result = a * b
    print("The result of multiplication is: ", result)
elif op == "/":
    if b != 0:
        result = a / b
        print("The result of division is: ", result)
    else:
        print("Error: Division by zero is not allowed.")

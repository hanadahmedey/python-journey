num1 = int(input("Enter your first number"))
operator = input("Enter operator (+, -, *, /, %, **, //)")
num2 = int(input("Enter your second number"))
if not type(num2) is int:
    raise ValueError("Only integers are allowed")
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error (cannot divide by zero)"
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
elif operator == "//":
    result = num1 // num2
else:
    result = "Invalid operator"
print("Result = ", result)
if not type(num1) is int:
    raise ValueError("Only integers are allowed")    







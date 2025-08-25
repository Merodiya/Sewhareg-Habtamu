import math

def calculator():
    print("📘 Scientific Calculator")
    print("Operations: +, -, *, /, sin, cos, tan")
    print("Type 'exit' to quit")

    while True:
        op = input("\nEnter operation (+, -, *, /, sin, cos, tan): ").lower()
        if op == "exit":
            print("Goodbye!")
            break

        # For trigonometry (single number, angle in degrees)
        if op in ["sin", "cos", "tan"]:
            x = float(input("Enter angle in degrees: "))
            rad = math.radians(x)   # convert degrees → radians

            if op == "sin":
                print(f"sin({x}) = {math.sin(rad)}")
            elif op == "cos":
                print(f"cos({x}) = {math.cos(rad)}")
            elif op == "tan":
                try:
                    print(f"tan({x}) = {math.tan(rad)}")
                except:
                    print("Undefined (tan is infinite here)")

        # For arithmetic (two numbers)
        elif op in ["+", "-", "*", "/"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if op == "+":
                print(f"{a} + {b} = {a + b}")
            elif op == "-":
                print(f"{a} - {b} = {a - b}")
            elif op == "*":
                print(f"{a} * {b} = {a * b}")
            elif op == "/":
                if b != 0:
                    print(f"{a} / {b} = {a / b}")
                else:
                    print("Error: Division by zero")

        else:
            print("❌ Invalid operation, try again.")

# Run calculator
calculator()

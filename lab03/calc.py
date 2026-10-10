num1 = float(input("Print first number: "))
num2 = float(input("Print second number: "))
operation = input("Choose operation: ")
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/" and num2 != 0:
    print(num1 / num2)
elif operation == "/" and num2 == 0:
    print("На ноль делить не стоит")

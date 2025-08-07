# Simple calculator

try:
    a = int(input("Enter the Second number: "))
    b = int(input("Enter the Second number: "))

    print("What kind of the operation you want to perform.\nPress + for addition \nPress - for Subtraction\nPress * for multiplicatin \nPress / for division")

    o = input("Enter the operation: ")

    match o:
        case "+":
            print(f"The result is {a + b}")
        case "-":
            print(f"The result is {a - b}")
        case "*":
            print(f"The result is {a * b}")
        case "/":
            print(f"The result is {a / b}")
        case default:
            print("Enter the valid number: ")


except Exception as e:
    print("Enter the valid value of a & b: ")
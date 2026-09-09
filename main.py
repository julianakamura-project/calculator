import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
}

repeat = True

while repeat:
    continue_calc = True
    print(art.logo)

    number1 = float(input("What is the first number?: "))
    while continue_calc:
        print("""
+
-
*
/
""")
        operation = input("Pick an operation: ")
        number2 = float(input("What is the next number?: "))
        result = operations[operation](number1, number2)

        print(f"{number1} {operation} {number2} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or type 'stop' to end calculation: ")
        if should_continue == "y":
            number1 = result
        elif should_continue == "n":
            print("\n" * 20)
            continue_calc = False
        elif should_continue == "stop":
            repeat = False
            print("Ending Calculator.")
            break
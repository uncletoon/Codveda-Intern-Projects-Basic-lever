def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
        if b == 0:
             raise ValueError("Error: B must be greater or less than to 0.")
        return a/b
    
        

def calculator():
    try:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))


        print("\n1. Addition (+)\n2. Substraction (-)\n3.Multiplication (*)\n4. Division (/).\n")
        choice = input("Select the Opretion (1-4 or + - * /):\n").strip()
    
        if choice in ('1', '+'):
            print(f"\nThe Sum of: {a} + {b} = {addition(a, b)}.\n")
        elif choice in ('2', '-'):
            print(f"\nThe Substraction of: {a} - {b} = {substraction(a, b)}.\n")
        elif choice in ('3', '*'):
            print(f"\nThe Multiplication of: {a} * {b} = {multiplication(a, b)}.\n")
        elif choice in ('4', '/'):
            try:
                print(f"\nThe Division of: {a} / {b} = {division(a, b)}.\n")
            except ValueError as e:
                print(e)
        
        else:
            print("Invalid operation selected. Please choose 1-4 or +-*/.\n")

    except ValueError :
        print("\nPlease enter the number.\n")


if __name__ == "__main__":
    calculator()

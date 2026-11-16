
# Function for addition
def addition(a, b):
    return a + b

# Function for subtraction
def subtraction(a, b):
    return a - b

# Function for multiplication
def multiplication(a, b):
    return a * b

# Function for division
def division(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

# While loop
while True:
    print("\n===== SIMPLE CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Choose an operation (1-4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Answer:", addition(num1, num2))

        elif choice == "2":
            print("Answer:", subtraction(num1, num2))

        elif choice == "3":
            print("Answer:", multiplication(num1, num2))

        elif choice == "4":
            print("Answer:", division(num1, num2))

    again = input("Do you want to continue? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the calculator!")
        break

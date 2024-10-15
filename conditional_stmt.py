# Function to perform the required operation based on the input string
def perform_operation(a, b, operation):
    if operation == "add":
        # If the operation is 'add', print the addition of a and b
        print("Addition of a and b is:", a + b)
    elif operation == "sub":
        # If the operation is 'sub', print the subtraction of a and b
        print("Subtraction of a and b is:", a - b)
    elif operation == "mul":
        # If the operation is 'mul', print the multiplication of a and b
        print("Multiplication of a and b is:", a * b)
    elif operation == "div":
        # If the operation is 'div', check if b is 0 to avoid divide by zero error
        if b == 0:
            # Print an error message if b is 0
            print("Division is not possible due to divide by zero error")
        else:
            # If b is not 0, print the division of a and b
            print("Division of a and b is:", a / b)
    else:
        # If the operation is not recognized, print an invalid operation message
        print("Invalid operation")

# Get the first float input from the user
a = float(input("Enter the first float value (a): "))

# Get the second float input from the user
b = float(input("Enter the second float value (b): "))
# Get the operation input from the user (add, sub, mul, div)
operation = input("Enter the operation (add, sub, mul, div): ")
# Call the function to perform the operation
perform_operation(a, b, operation)

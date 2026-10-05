while True:

    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
    

        operation = input("Enter the operation (+, -, *, /): ")

        if operation  == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "*":
            result = number1 * number2
        elif operation == "/":
            result = number1 / number2
        print("result:", result)
        
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != "yes":
                break
        
    except ValueError:
        print("please enter a number.")
        
        
    
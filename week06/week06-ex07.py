def input_validation():
    while True:
        user_input = int(input("Enter an integer between 1 and 10 inclusive: "))
        if 1 <= user_input <= 10:
            print("OK")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 10.")

input_validation()

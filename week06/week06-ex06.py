def accumulate_sum():
    total = 0
    while True:
        user_input = int(input("Enter an integer (0 to stop): "))
        if user_input == 0:
            break
        total += user_input
    
    print(f"The sum of all non-zero integers is: {total}")

accumulate_sum()

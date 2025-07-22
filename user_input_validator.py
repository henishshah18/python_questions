while True:
    user_input = input("Enter your age (1–120): ").strip()
    
    if user_input == "":
        print("Input cannot be empty. Please enter a valid number.")
        continue

    try:
        age = int(user_input)
        if 1 <= age <= 120:
            print(f"\nYou entered a valid age: {age}")
            break
        else:
            print("Out of range. Please enter a number between 1 and 120.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

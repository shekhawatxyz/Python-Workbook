while True:
    height = float(input("Please enter your height in metres: "))
    weight = float(input("Please enter your weight in kilograms: "))
    if height <= 0 or weight <= 0:
        print("Enter positive values.")
    print(f"BMI - {weight / (height**2)}.")
    break

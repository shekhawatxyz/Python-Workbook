while True:
    p = float(input("Enter the principle amount in dollars: "))
    if p <= 0:
        print("Please enter a positive natural number")
    else:
        np = p * ((1 + 0.04) ** 3)
        print(f"The amount post three years ${np:,.2f}")
        break

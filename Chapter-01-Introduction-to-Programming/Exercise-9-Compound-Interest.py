while True:
    p = float(input("Enter the principle amount in dollars: "))
    if p <= 0:
        print("Please enter a positive natural number")
    else:
        p = p * ((1 + 0.04) ** 1)
        print(f"The amount post year one ${p:,.2f}")
        p = p * ((1 + 0.04) ** 1)
        print(f"The amount post year two ${p:,.2f}")
        p = p * ((1 + 0.04) ** 1)
        print(f"The amount post year three ${p:,.2f}")
        break

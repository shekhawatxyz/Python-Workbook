while True:
    loaves = int(input("Enter the number of day-old loaves of bread you want: "))
    if loaves <= 0:
        print("Please enter a positive amount.")
    price = 3.49
    dis_price = 3.49 * 0.40
    print(f"The regular price for bread here is {price}")
    print(f"The price for day-old bread here is {dis_price:.2f}")
    print(
        f"The total bill for your {loaves} loaves of day-old bread is {loaves * dis_price}."
    )
    break

d = 0
while True:
    a = input("Enter the age of the guest, enter a blank to get the total cost: ")
    if a == "":
        print(f"The total cost of admission is ${d:.2f}!")
        break
    else:
        b = float(a)
        b = int(b)
        if b >= 65:
            d += 18
        elif b >= 13:
            d += 23
        elif b >= 3:
            d += 14
        else:
            d += 0

while True:
    m = float(input("Enter the mass of water: "))
    t = float(input("Enter the temperature change of the water: "))
    if m <= 0 or t <= 0:
        print("Enter a postive number.")
    c = 4.186
    q = m * t * c
    print(f"The total heat is {q} and {8.9 * 2.77778e-7 * q} is the cost")
    break

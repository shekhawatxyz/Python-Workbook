while True:
    h = float(input("Enter the height of the triangle: "))
    b = float(input("Enter the base of the triangle: "))
    if h <= 0 or b <= 0:
        print("Enter a positive value.")
    print(f"The area of the triangle is {0.5 * h * b}.")
    break

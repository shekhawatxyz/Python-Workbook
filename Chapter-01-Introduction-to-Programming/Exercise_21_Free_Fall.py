while True:
    h = float(input("Enter the height of the object: "))
    if h <= 0:
        print("Enter a positive height.")
    g = 9.8
    vi = 0
    vf = (((vi) ** 2) + (2 * g * h)) ** 0.5
    print(f"The final velocity is {vf}.")
    break

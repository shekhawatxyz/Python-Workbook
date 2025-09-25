while True:
    side = int(input("Enter the number of sides in the shape: "))
    shapes = {
        3: "triangle",
        4: "quadilateral",
        5: "pentagon",
        6: "hexagon",
        7: "septagon",
        8: "octagon",
        9: "nonagon",
        10: "decagon",
    }
    if side <= 2 or side >= 11:
        print("Enter a positive number below 11 and above 2.")
    else:
        print(f"{shapes[side]}")
        break

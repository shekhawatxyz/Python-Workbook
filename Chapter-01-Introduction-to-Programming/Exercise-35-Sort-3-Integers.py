while True:
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))
    c = int(input("Enter the third integer: "))
    big = max(a, b, c)
    small = min(a, b, c)
    mid = (a + b + c) - big - small
    print(f"{big} {mid} {small}")
    break

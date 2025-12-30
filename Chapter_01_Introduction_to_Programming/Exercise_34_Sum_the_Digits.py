while True:
    a = input("Enter a four digit number: ")
    if len(a) != 4:
        print("Enter a four digit number please.")
    b = int(a)
    if b < 0:
        print("Enter a positive number please.")
    print(
        f"The sum of the number {int(a)} is {int(a[0]) + int(a[1]) + int(a[2]) + int(a[3])}."
    )
    break

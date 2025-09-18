while True:
    n = int(input("Enter a positive whole number "))
    if n <= 0:
        print("Please enter a positive whole number ")
    else:
        sum = ((n) * (n + 1)) / 2
        print(f"sum is {sum:,}")
        break

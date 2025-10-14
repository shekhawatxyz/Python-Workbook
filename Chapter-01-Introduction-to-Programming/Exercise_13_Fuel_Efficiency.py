a = float(input("Enter the fuel efficiency in MPG: "))
while True:
    if a <= 0:
        print("Please enter a positive number.")
        continue
    else:
        print(f"{a * 235.22}")
        break

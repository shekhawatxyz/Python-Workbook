a = float(input("Enter the rating please: "))
if a >= 0.6:
    print("Meritorius Performance!")
    print(f"The raise is ${a * 2400}!")
elif a == 0.4:
    print("Acceptable Performance!")
    print(f"The raise is ${a * 2400}!")
elif a == 0.0:
    print("Unacceptable Performance!")
    print(f"The raise is ${a * 2400}!")
else:
    print("Enter a suitable amount please.")

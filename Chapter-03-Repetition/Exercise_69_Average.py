a = 1
v = 0
n = 0
print("You will enter integers you want averaged, enter 0 when you wish to stop")
while a == 1:
    b = int(input("Enter integer: "))
    v += b
    n += 1
    if b == 0:
        if n == 1:
            print("Your first value was zero, restart the program!")
            a = 0
        else:
            print(f"The average is {(v / (n - 1)):.2f}!")
            a = 0

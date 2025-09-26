s = float(input("Enter the speed: "))
p = 0
d = 0
if s >= 50:
    p = str(p)
    p = "going to be decided by a judge"
    d = 7
    print(
        f"The penalty is {p} and the demerit ponits are {d} for driving at an excessive speed of {s}."
    )
elif s >= 30:
    p = 7.00
    d = 4
    print(
        f"The penalty is {p} and the demerit ponits are {d} for driving at an excessive speed of {s}."
    )
elif s >= 20:
    p = 4.50
    d = 3
    print(
        f"The penalty is {p} and the demerit ponits are {d} for driving at an excessive speed of {s}."
    )
elif s >= 16:
    p = 3.00
    d = 3
    print(
        f"The penalty is {p} and the demerit ponits are {d} for driving at an excessive speed of {s}."
    )
elif s >= 1:
    p = 3.00
    d = 0
    print(
        f"The penalty is {p} and the demerit ponits are {d} for driving at an excessive speed of {s}."
    )
else:
    print("Not speeding if speed is low.")

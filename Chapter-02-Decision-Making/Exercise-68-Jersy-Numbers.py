n = int(input("Enter the number: "))
p = int(input("Enter 1 for offence and 0 for defence: "))
if n not in range(1, 100):
    print("You entered incorrect an Jersey number")
if p not in range(0, 2):
    print("Please select offence or defence")
pos = []
if p == 1:
    if n in range(1, 20):
        pos.append("Qaurterback")
        pos.append("Punter and placekicker")
    if n in range(10, 20) or n in range(80, 90):
        pos.append("Wide receiver")
    if n in range(20, 50):
        pos.append("Running back")
    if n in range(80, 90) or n in range(40, 50):
        pos.append("Tight end")
    if n in range(50, 80):
        pos.append("Offensive lineman")
    if len(pos) == 0:
        print("Number not found in offensive positions")
    else:
        print("The corresponding number could belong to the following positions: ")
        for a in pos:
            print(a)
else:
    if n in range(20, 50):
        pos.append("Defensive back")
    if n in range(50, 80) or n in range(90, 100):
        pos.append("Defensive lineman")
    if n in range(40, 60) or n in range(90, 100):
        pos.append("Linebacker")
    if len(pos) == 0:
        print("Number not found in defensive positions")
    else:
        print("The corresponding number could belong to the following positions: ")
        for a in pos:
            print(a)

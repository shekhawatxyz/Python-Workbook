import random

while True:
    d = input("Enter the dice notation, enter blank to quit: ")
    if d == "":
        break
    elif "d" in d:
        b = False
        c = d.split("d")
        if c[0] == "":
            print(random.randint(1, int(c[1])))
        else:
            n = int(c[0])
            s = int(c[1])
            t = 0
            for j in range(n):
                f = random.randint(1, s)
                print(f)
                t += f
            print(t)

    else:
        print("Please enter the notations correctly!")

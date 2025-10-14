d = []
gp = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0,
}
while True:
    a = input("Enter the letter grades, enter blank to get the output: ")
    if a == "":
        print(f" Average grade point is : {sum(d) / len(d)}")
        break
    elif a in gp:
        d.append(gp[a])

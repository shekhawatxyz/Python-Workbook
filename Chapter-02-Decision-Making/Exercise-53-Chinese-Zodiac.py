y = int(input("Enter the year: "))
n = [
    "Monkey",
    "Rooster",
    "Dog",
    "Pig",
    "Rat",
    "Ox",
    "Tiger",
    "Hare",
    "Dragon",
    "Snake",
    "Horse",
    "Sheep",
]

print(f"{n[y % 12]}")

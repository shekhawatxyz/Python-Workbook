a = input("Enter a month: ")
a = a.capitalize()
birthstones = {
    "January": "Garnet",
    "February": "Amethyst",
    "March": "Aquamarine and Bloodstone",
    "April": "Diamond",
    "May": "Emerald",
    "June": "Pearl, Alexandrite and Moonstone",
    "July": "Ruby",
    "August": "Peridot, Spinel and Sardonyx",
    "September": "Sapphire",
    "October": "Opal and Tourmaline",
    "November": "Topaz and Citrine",
    "December": "Tanzanite, Turquoise and Zicron",
}

if a in birthstones:
    print(f"{birthstones[a]}")
else:
    print(f"{a} is not a valid month.")

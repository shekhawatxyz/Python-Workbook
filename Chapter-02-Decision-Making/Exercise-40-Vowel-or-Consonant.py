while True:
    a = input("Enter an alphabet: ")
    a = a.lower()
    vowels = ["a", "e", "i", "o", "u"]
    if a == "y":
        print("Sometimes y is a vowel, sometimes it's a consonant.")
    elif a in vowels:
        print(f"{a} is a vowel.")
    else:
        print(f"{a} is a consonant.")
    break

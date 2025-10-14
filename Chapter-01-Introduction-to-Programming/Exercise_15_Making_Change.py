while True:
    a = int(input("Enter the amount in cents: "))
    # penny = 1, nickel = 5, dime = 10, quarter = 25, loonie = 100, toonie = 200
    # coin conversion
    penny = 0
    nickel = 0
    dime = 0
    quarter = 0
    loonie = 0
    toonie = 0
    if a <= 0:
        print("Please enter a positive number")
    while a != 0:
        if a >= 200:
            a -= 200
            toonie += 1
        if a >= 100:
            a -= 100
            loonie += 1
        if a >= 25:
            a -= 25
            quarter += 1
        if a >= 10:
            a -= 10
            dime += 1
        if a >= 5:
            a -= 5
            nickel += 1
        if a >= 1:
            a -= 1
            penny += 1
    print(
        f"you will be given {toonie} toonies, {loonie} loonies, {quarter} quarters,{nickel} nickels,{dime} dimes,{penny} pennis."
    )
    break

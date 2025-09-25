while True:
    a = input("Enter the month: ")
    a = a.lower()
    b = ["january", "march", "may", "july", "august", "october", "december"]
    c = ["april", "june", "september", "november"]
    if a == "february":
        print("28 or 29 days")
    elif a in b:
        print("31 days")
    elif a in c:
        print("30 days")
    break

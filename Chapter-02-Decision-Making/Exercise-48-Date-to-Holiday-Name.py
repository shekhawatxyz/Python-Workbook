a = input("Enter a month: ")
b = int(input("Enter a day: "))
if a.lower() == "january" and b == 1:
    print("New Year's Day")
elif a.lower() == "july" and b == 1:
    print("Canada Day")
elif a.lower() == "december" and b == 25:
    print("Christmas Day")
else:
    print("Not in the calendar")

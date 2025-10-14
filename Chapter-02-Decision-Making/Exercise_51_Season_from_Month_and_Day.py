m = input("Enter the month: ").capitalize()
d = int(input("Enter the date: "))
s = m + " " + str(d)
print(s)
calendar = {
    "Spring": "March 20",
    "Summer": "June 21",
    "Fall": "September 22",
    "Winter": "December 21",
}
for key, values in calendar.items():
    if s == values:
        print(f"{key}")
        break

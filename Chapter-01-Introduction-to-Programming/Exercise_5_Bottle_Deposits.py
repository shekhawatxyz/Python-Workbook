small = int(
    input("Enter the number of bottles that hold a litre or less you have to return ")
)
large = int(
    input("Enter the number of bottles that hold more than a litre you have to return ")
)
print(f"{((small * 0.10) + (large * 0.25)):,} dollars is the total amount refunded.")

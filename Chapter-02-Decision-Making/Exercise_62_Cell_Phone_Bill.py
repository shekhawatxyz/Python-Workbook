m = float(input("Enter the number of minutes: "))
t = float(input("Enter the number of texts: "))
et = 0
if t > 50:
    et += (t - 50) * 0.25
em = 0
if m > 50:
    em += (m - 50) * 0.15
ec = 0.44
b = 15 + et + em + ec
tb = b + (b * 0.05)
print("Base charge is $15.00")
if em != 0:
    print(
        f"Additional minute charge is ${em:.2f} for {m - 50} extra minutes, every extra minute costing $0.25"
    )
if et != 0:
    print(
        f"Additional minute charge is ${et:.2f} for {t - 50} extra minutes, every extra minute costing $0.15"
    )
print(f"911 charge is ${ec:.2f}")
print(f"The tax is all charges plus 5 percent")
print(f"The total bill is ${tb:.2f}")

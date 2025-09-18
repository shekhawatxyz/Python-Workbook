bill = float(input("Enter the bill amount: "))
bill_tax = (0.05 * bill) + bill
tip = bill_tax * 0.2
print(f"Your bill after taxes ${bill_tax:,.2f} and the tip ${tip:,.2f}.")

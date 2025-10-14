i = input("Enter the number: ")
i = i.replace(",", "")
p = len(i)
t = 0
for j in i:
    t += int(j) ** p
if t == int(i):
    print("Armstrong number!")
else:
    print("Not an armstrong number!")

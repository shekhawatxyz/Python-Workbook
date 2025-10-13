# t = 0
# e = []
# for i in range(11):
#     c = input("Enter the digits of the code: ")
#     e.append(c)
#     print(e)
# for i in range(12):
#     if i % 2 == 0:
#         t += 3 * (int(e[i]))
#     else:
#         t += int(e[i])
# if t % 10 == 10:
#     print("check digit is zero")
# else:
#     print(f"{10 - (t % 10)}")
d = ""
li = []
t = 0
while True:
    if len(li) == 11:
        break
    else:
        d = input("Enter digits of the code: ")
        li.append(d)
        print(li)
for i, c in enumerate(li):
    if i % 2 == 0:
        t += 3 * int(c)
        print(t)
    else:
        t += int(c)
        print(t)

a = input("Enter the word: ")
a = a.lower()
p = 0
np = 0
for i, c in enumerate(a):
    if a[i] != a[len(a) - 1 - i]:
        np += 1
    else:
        p += 0
if np != 0:
    print(f"{a} not a palindrome")
else:
    print(f"{a} is a palindrome")

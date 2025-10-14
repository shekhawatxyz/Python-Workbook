import string

l = string.ascii_lowercase

# a = input("Enter the string to check if it is a palindrome or not: ")
a = input("Enter the string to check if it ends in a palindrome: ")
na = ""
b = a.lower()
for c in b:
    if c in l:
        na = na + c
    else:
        pass
p = True
i = 0
while p and i < len(na) / 2:
    if na[i] != na[len(na) - i - 1]:
        p = False
    i += 1
if p != True:
    print(f"{a} is not a palindrome")
else:
    print(f"{a} is a palindrome")

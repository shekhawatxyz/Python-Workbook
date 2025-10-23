sc = [".", "?", "!"]
# s = f"      what time do i have to be there? what’s the address? this time i’ll try to be on time!"
s = input("Enter string: ")
print(s)
a = s.strip()
a = a.capitalize()
print(a.capitalize())
n = ""
for i, c in enumerate(a):
    if a[i - 2] in sc:
        n = n + c.capitalize()
    elif c == "i" and a[i - 1] == " ":
        if i <= len(a) - 1:
            n = n + c.capitalize()
        elif a[i + 1] in sc or a[i + 1] == " ":
            n = n + c.capitalize()
    else:
        n = n + c
print(n)

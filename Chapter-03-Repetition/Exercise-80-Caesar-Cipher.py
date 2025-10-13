import string

lowercase = list(string.ascii_lowercase)
# print(lowercase)
uppercase = list(string.ascii_uppercase)
l = 26
# print(len(uppercase))

a = input("Enter the characters please: ")
b = []
for c in a:
    b.append(c)
shift = int(input("Enter the shift please: "))

for i, c in enumerate(b):
    if c in uppercase:
        v = uppercase.index(c)
        if shift > 0:
            d = v + shift
            if d >= 25:
                d = d % 26
                print(uppercase[d])
            else:
                print(uppercase[d])
        elif shift < 0:
            d = v + shift
            print(uppercase[d])
    elif c in lowercase:
        v = lowercase.index(c)
        if shift > 0:
            d = v + shift
            if d >= 25:
                d = d % 26
                print(lowercase[d])
            else:
                print(lowercase[d])
        elif shift < 0:
            d = v + shift
            print(lowercase[d])
    else:
        print(c)

a = 7
b = 4
c = 4


def valid_triangle(a, b, c):
    assert type(a) is int or float
    assert type(b) is int or float
    assert type(c) is int or float
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True


a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))
d = valid_triangle(a, b, c)
if d:
    print("Valid")
else:
    print("Invalid")

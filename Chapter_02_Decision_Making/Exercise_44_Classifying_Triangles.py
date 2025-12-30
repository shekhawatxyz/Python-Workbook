a = float(input("Length of the first side of the triagle: "))
b = float(input("Length of the second side of the triagle: "))
c = float(input("Length of the third side of the triagle: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Enter real lengths")
elif a == b == c:
    print("Equilateral triangle")
elif a != b != c:
    print("Scalene triangle")
else:
    print("Isosceles triangle")

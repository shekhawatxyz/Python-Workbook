while True:
    s1 = float(input("Enter length of the first side of the triangle: "))
    s2 = float(input("Enter length of the second side of the triangle: "))
    s3 = float(input("Enter length of the third side of the triangle: "))
    if s1 <= 0 or s2 <= 0 or s3 <= 0:
        print("Enter positive values.")
    if s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
        print("Please enter correct values.")
    s = (s1 + s2 + s3) / 2
    area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
    print(f"The area of the triangle is {area}.")
    break

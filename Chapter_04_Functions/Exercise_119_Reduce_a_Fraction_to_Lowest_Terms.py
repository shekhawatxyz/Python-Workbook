# import sys
# import os
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# if project_root not in sys.path:
#    sys.path.insert(0,project_root)
# from Chapter_03_Repetition.Exercise_87_Greatest_Common_Divisor import
def lowest_fraction(n, m):
    # n = 72
    # m = 46
    # n = int(input("Enter an integer: "))
    # m = int(input("Enter an integer: "))
    d = min(n, m)
    while n % d != 0 or m % d != 0:
        d -= 1
    # print(d)
    return f"{n // d}/{m // d}"


def main():
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denomenator: "))
    print(lowest_fraction(a, b))


if __name__ == "__main__":
    main()

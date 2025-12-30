def n_median(a, b, c):
    d = [a, b, c]
    d.sort()
    return d[1]


def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    print(f"{n_median(a, b, c)}")


if __name__ == "__main__":
    main()

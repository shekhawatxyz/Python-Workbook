def fare(d):
    fr = 4 + (d * 1000) * (0.25 / 140)
    return fr


def main():
    d = int(input("Enter the kilometers: "))
    print(f"{fare(d):.2f}")


if __name__ == "__main__":
    main()

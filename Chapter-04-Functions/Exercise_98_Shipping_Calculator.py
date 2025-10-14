def cost(items):
    assert items >= 0
    return 10.95 + (2.95 * (items - 1))


def main():
    items = int(input("Enter the number of items: "))
    print(cost(items))


if __name__ == "__main__":
    main()

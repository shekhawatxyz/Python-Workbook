def isInteger(a):
    a = a.strip()
    if (a[0] == "+" or a[0] == "-") and a[1:].isdigit():
        return True
    if a.isdigit():
        return True
    return False


def main():
    a = input("Enter the the integer: ")
    if isInteger(a):
        print("int")
    else:
        print("not int")


if __name__ == "__main__":
    main()

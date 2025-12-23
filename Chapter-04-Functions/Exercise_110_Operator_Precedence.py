def precedence(a):
    if a == "^":
        return 3
    elif a == "*" or a == "/":
        return 2
    elif a == "+" or a == "-":
        return 1
    else:
        return -1


def main():
    a = input("Enter the operator: ")
    print(precedence(a))


if __name__ == "__main__":
    main()

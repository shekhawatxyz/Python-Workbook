def isprime(a):
    if int(a) <= 1:
        return "it should be above 1"
    a = int(a)
    for c in range(2, a - 1):
        if a % c == 0:
            return False
    return True


def main():
    a = input("Enter the number: ")
    print(isprime(a))


if __name__ == "__main__":
    main()

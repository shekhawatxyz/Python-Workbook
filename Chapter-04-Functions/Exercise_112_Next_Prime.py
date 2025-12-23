from Exercise_111_Is_a_Number_Prime import *


def main():
    a = int(input("Enter a number: "))
    if isprime(a):
        a += 1

    while not isprime(a):
        a += 1

    return a


if __name__ == "__main__":
    print(main())

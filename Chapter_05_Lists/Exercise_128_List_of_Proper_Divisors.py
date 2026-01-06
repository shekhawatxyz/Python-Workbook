# num = 12
def list_of_proper_divisors(num):
    # num = int(input("Enter the number: "))
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(int(i))
    return divisors


def main():
    n = int(input("Enter a number: "))
    print(list_of_proper_divisors(n))


if __name__ == "__main__":
    main()

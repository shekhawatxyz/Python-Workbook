import random


def generate_password():
    a = random.randint(7, 10)
    f = ""
    for _ in range(a):
        d = chr(random.randint(33, 126))
        print(f"{d}", end="")
        f = f + d
    print()
    return f


def main():
    generate_password()


if __name__ == "__main__":
    main()

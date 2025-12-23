import random


def license_plate_generator():
    l = ""

    for _ in range(random.randint(3, 4)):
        a = random.randint(0, 9)
        l = l + str(a)

    for _ in range(3):
        a = chr(random.randint(65, 91))
        l = l + str(a)

    return l


def main():
    print(license_plate_generator())


if __name__ == "__main__":
    main()

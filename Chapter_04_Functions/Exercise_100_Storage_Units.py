def storage_units(a):
    assert a > 0
    p = ""
    n = 0
    if a >= 2**40:
        p = "TiB"
        n = a / 2**40
    elif a >= 2**30:
        p = "GiB"
        n = a / 2**30
    elif a >= 2**20:
        p = "MiB"
        n = a / 2**20
    else:
        p = "KiB"
        n = a / 2**10
    return f"{n:.2f}{p}"


def main():
    a = int(input("Enter the number of bytes: "))
    print(storage_units(a))


if __name__ == "__main__":
    main()

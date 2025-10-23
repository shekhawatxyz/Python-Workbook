def spacing(s, w):
    s = str(s)
    w = int(w)
    assert type(w) is int
    assert type(s) is str
    css = f"{s:^{w}}"
    final = f"'{css}'"
    return final


def main():
    s = input("Enter the string: ")
    w = int(input("Enter the spacing integer: "))
    n = spacing(s, w)
    print(n)


if __name__ == "__main__":
    main()

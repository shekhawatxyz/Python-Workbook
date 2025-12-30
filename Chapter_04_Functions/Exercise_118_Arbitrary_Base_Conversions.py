def convert_to_decimal(n, b):
    # n = 3
    # b = "1200"
    assert type(n) is str
    assert type(b) is int
    d = 0
    l = len(n) - 1
    for c in n:
        f = int(c) * b**l
        d += f
        l -= 1
    return d


def convert_to_base(n, b):
    assert type(n) is int
    assert type(b) is int
    assert b >= 2 and b <= 16
    # q = int(input("Enter the number to convert: ")
    c = ""
    while n != 0:
        r = n % b
        # c = str(r)+c
        c = "0123456789ABCDEF"[r] + c
        n = n // b
    return c


print(convert_to_base(255, 16))

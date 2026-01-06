# def only_the_words(s):
# s = "Contractions include: don’t, isn’t, and wouldn’t."
# s = s.split()
# print(s)
def only_the_words(s):
    s = s.split()
    new = []
    symbols = [":", "-", "?", ".", ";", '"', "'", ","]
    for a in s:
        if a[0] in symbols:
            # a.remove()
            a = a[1:]
        if a[-1] in symbols:
            a = a[:-1]
        new.append(a)
    return new


def main():
    s = input("Enter a string: ")
    print(only_the_words(s))


if __name__ == "__main__":
    main()

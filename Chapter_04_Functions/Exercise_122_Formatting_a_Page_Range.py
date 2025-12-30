def formatted_page_range(lower_page_number, higher_page_number):
    if (
        lower_page_number < 100
        or lower_page_number % 100 == 0
        or len(str(higher_page_number)) > len(str(lower_page_number))
    ):
        return f"{lower_page_number}-{higher_page_number}"
    else:
        h = list(map((str), str(higher_page_number)))
        l = list(map((str), str(lower_page_number)))
        # h = higher_page_number.split()
        # print(h)
        for i, c in enumerate(l):
            if c != h[i]:
                return f"{lower_page_number}-{''.join(h[i:])}"


def main():
    lower_page_number = int(input("Enter the lower page number: "))
    higher_page_number = int(input("Enter the higher page number: "))
    print(formatted_page_range(lower_page_number, higher_page_number))


if __name__ == "__main__":
    main()

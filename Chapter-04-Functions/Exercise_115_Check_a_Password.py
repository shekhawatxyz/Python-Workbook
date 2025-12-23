def check_password(password):
    lower = 0
    upper = 0
    number = 0
    if len(password) >= 8:
        for p in password:
            if p.islower():
                lower += 1
            elif p.isupper():
                upper += 1
            elif p.isnumeric():
                number += 1
    if lower >= 1 and upper >= 1 and number >= 1:
        return True
    return False


# print(check_password(password))
def main():
    a = input()
    print(check_password(a))


if __name__ == "__main__":
    main()

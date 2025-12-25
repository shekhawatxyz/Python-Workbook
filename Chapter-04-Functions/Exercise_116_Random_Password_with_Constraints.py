from random import randint
from Exercise_113_Random_Password import generate_password
from Exercise_115_Check_a_Password import check_password


def main():
    count = 0
    while True:
        a = generate_password()
        if check_password(a):
            print(check_password(a))
            print(count)
            break
        count += 1


if __name__ == "__main__":
    main()

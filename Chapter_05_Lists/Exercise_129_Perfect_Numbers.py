from Exercise_128_List_of_Proper_Divisors import list_of_proper_divisors


def perfect_number(n):
    if sum(list_of_proper_divisors(n)) == n:
        return True
    else:
        return False


def main():
    perfect_numbers = []
    for i in range(1, 10000):
        if perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers


print(main())
# print(perfect_number(28))

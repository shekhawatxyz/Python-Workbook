def sorted_order():
    nums = []
    num = input("Enter a number, or enter a 0 to stop: ")
    while int(num) != 0:
        n = int(num)
        nums.append(n)

        num = input("Enter a number, or enter a 0 to stop: ")

    b = sorted(nums)
    for c in b:
        print(c)


sorted_order()

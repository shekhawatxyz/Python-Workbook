nums = []
num = input("Enter a number, enter 0 to stop: ")
while int(num) != 0:
    n = int(num)
    nums.append(n)

    num = input("Enter a number, enter 0 to stop: ")

b = sorted(nums, reverse=True)
print(b)

def remove_outliers(ls: list, n: int) -> list:
    assert len(ls) >= 4
    nls = sorted(ls, reverse=True)
    for _ in range(n):
        nls.pop()
    nls.sort()
    for _ in range(n):
        nls.pop()
    return nls


# nums = [10,2,5,3,4,7,9,1]
# n = 1
# print(remove_outliers(nums,n))
def main():
    nums = []
    num = input("Enter a number, enter 0 to stop")

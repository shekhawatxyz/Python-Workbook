# a = [3,-4,1,0,-1,0,-2]
a = []
inp = input("Enter numbers, enter a blank to stop: ")
while inp != "":
    a.append(int(inp))
    inp = input("Enter numbers, enter a blank to stop: ")

negative_nums = []
zero_nums = []
positive_nums = []
for b in a:
    if b > 0:
        positive_nums.append(b)
    elif b < 0:
        negative_nums.append(b)
    else:
        zero_nums.append(b)
joined_list = negative_nums + zero_nums + positive_nums
for c in joined_list:
    print(c)

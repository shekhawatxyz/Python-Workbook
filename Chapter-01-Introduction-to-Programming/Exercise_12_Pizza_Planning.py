import math

a = int(input("Please enter the number of people: "))
b = int(input("Enter the number of slices of pizza per person: "))
c = (a * b) / 8
print(f"number of pizzas needed is {math.ceil(c)}")

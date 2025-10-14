import math

a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))

# Basic arithmetic operations
print(f"The sum of a and b is {a + b}.")
print(f"The difference when b is subtracted from a is {a - b}.")
print(f"The product of a and b is {a * b}.")
print(f"The quotient when a is divided by b is {a / b}.")
print(f"The remainder when a is divided by b is {a % b}.")

# Logarithm with a Unicode subscript
print(f"The result of 'log\u2081\u2080(a)' is {math.log10(a)}")

# Exponentiation with a Unicode superscript
print(f"The result of 'a\u1d47' is {a**b}.")

a = float(input("Enter the frequency in Hz : "))
if a >= 3 * 10**19:
    print("Gamma Rays")
elif a >= 3 * 10**17:
    print("X-Rays")
elif a >= 7.5 * 10**14:
    print("Ultraviolet Light")
elif a >= 4.3 * 10**14:
    print("Visible Light")
elif a >= 3 * 10**12:
    print("Infrared Light")
elif a >= 3 * 10**9:
    print("Microwaves")
elif a < 3 * 10**9:
    print("Radio Waves")

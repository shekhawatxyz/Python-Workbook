while True:
    ta = float(input("Enter the air temperature in Celsius: "))
    v = float(input("Enter the wind speed in kilometers per hour: "))
    if ta > 10 or v <= 4.8:
        print(
            "Please enter again, its only valid for temperatures equal to or below 10 degrees celsius and wind speeds exceeding 4.8 kmph."
        )
    print(
        f"{(13.12 + (0.6215 * ta) - (11.37 * (v**0.16)) + (0.3965 * ta * (v**0.16)))}"
    )
    break

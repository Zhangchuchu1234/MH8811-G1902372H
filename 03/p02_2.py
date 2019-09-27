def CelsiusFahrenheitConverter():
    CelsiusTemp = input("Input a number for the temperature in Celsius: ")
    while not CelsiusTemp:
        CelsiusTemp = input("Input a number for the temperature in Celsius: ")

    try:
        FahrenheitTemp = float(CelsiusTemp) * 1.8 + 32
        print("When the temperature in Celsius is {0}, temperature in Fahrenheit is {1:5.3f}".format(CelsiusTemp, FahrenheitTemp))
    except ValueError:
        print("Error, your input for the temperature is not a number. ")

    return

def convCtoF(c):
    f = 9/5*c+32
    return f
celsiusTemperature = [12,45,6,78,5,26,67]
print("Temperature is celsius:",celsiusTemperature)

FahrenhitTemperature =[]
for t in celsiusTemperature:
    x = convCtoF(t)
    FahrenhitTemperature.append(x)
print("Temperature in Fahrenheit:",FahrenhitTemperature)

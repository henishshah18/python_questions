def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 1)

def fahrenheit_to_kelvin(fahrenheit):
    return round(((fahrenheit - 32) * 5/9) + 273.15, 2)

def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)


# Sample function calls and formatted output
c = 0
f = celsius_to_fahrenheit(c)
print(f"{c}°C = {f}°F")

f = 32
k = fahrenheit_to_kelvin(f)
print(f"{f}°F = {k}K")

k = 300
c = kelvin_to_celsius(k)
print(f"{k}K = {c}°C")

temperatura_celsius = float(input("Insira a temperatura em Celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
temperatura_kelvin = temperatura_celsius + 273.15

print(
    (
        f"{temperatura_celsius:.2f}° Celsius equivale a "
        f"{temperatura_fahrenheit:.2f}° Fahrenheit e "
        f"{temperatura_kelvin:.2f} Kelvin."
    )
)

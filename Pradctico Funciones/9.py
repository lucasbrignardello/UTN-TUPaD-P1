def celsius_a_fahrenheit(celsius):
    """Devuelve el equivalente en Fahrenheit de la temperatura en Celsius."""
    return celsius * 9 / 5 + 32

if __name__ == "__main__":
    try:
        entrada = input("Ingrese la temperatura en Celsius: ").strip()
        c = float(entrada)
        f = celsius_a_fahrenheit(c)
        print(f"{c} °C equivalen a {round(f, 2)} °F")
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número.")
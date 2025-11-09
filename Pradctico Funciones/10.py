def calcular_promedio(a, b, c):
    """
    Devuelve el promedio de tres números.
    """
    return (a + b + c) / 3


if __name__ == "__main__":
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        c = float(input("Ingrese el tercer número: "))
    except ValueError:
        print("Entrada inválida. Por favor, introduzca números.")
    else:
        promedio = calcular_promedio(a, b, c)
        print(f"El promedio es: {promedio}")
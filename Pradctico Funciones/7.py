def operaciones_basicas(a, b):
    """
    Devuelve una tupla: (suma, resta, multiplicacion, division)
    Si b es 0, la división será None.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multiplicacion, division)

def main():
    try:
        a = float(input("Ingrese el primer número (a): ").strip())
        b = float(input("Ingrese el segundo número (b): ").strip())
    except ValueError:
        print("Entrada inválida: por favor ingrese números.")
        return

    suma, resta, multiplicacion, division = operaciones_basicas(a, b)

    print(f"\nResultados para a = {a} y b = {b}:")
    print(f"- Suma: {suma}")
    print(f"- Resta: {resta}")
    print(f"- Multiplicación: {multiplicacion}")
    if division is None:
        print("- División: No se puede dividir por cero.")
    else:
        print(f"- División: {division}")

if __name__ == "__main__":
    main()
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

if __name__ == "__main__":
    try:
        n = int(input("Ingrese un número: "))
    except ValueError:
        print("Entrada no válida. Por favor ingrese un número entero.")
    else:
        tabla_multiplicar(n)
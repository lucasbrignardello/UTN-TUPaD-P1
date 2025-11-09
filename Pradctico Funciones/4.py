import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def main():
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            if radio < 0:
                print("El radio no puede ser negativo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Introduzca un número válido.")

    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f"Área: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")

if __name__ == "__main__":
    main()
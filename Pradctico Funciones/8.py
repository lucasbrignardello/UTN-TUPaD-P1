def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).
    Args:
        peso (float): peso en kilogramos
        altura (float): altura en metros
    Returns:
        float: IMC redondeado a dos decimales
    """
    if altura <= 0:
        raise ValueError("La altura debe ser un número positivo mayor que cero.")
    imc = peso / (altura ** 2)
    return round(imc, 2)


def main():
    try:
        peso = float(input("Ingrese el peso en kg: ").strip())
        altura = float(input("Ingrese la altura en metros: ").strip())
        if peso <= 0 or altura <= 0:
            print("Peso y altura deben ser números positivos.")
            return
    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar números (ejemplo: 70.5).")
        return

    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc}")


if __name__ == "__main__":
    main()
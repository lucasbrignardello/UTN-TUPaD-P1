def segundos_a_horas(segundos):
    """Convierte segundos a horas (float)."""
    return segundos / 3600

if __name__ == "__main__":
    try:
        s = float(input("Ingrese la cantidad de segundos: "))
    except ValueError:
        print("Entrada no válida. Introduzca un número.")
    else:
        horas = segundos_a_horas(s)
        print(f"{s} segundos = {horas} horas")
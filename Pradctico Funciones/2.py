def saludar_usuario(nombre: str) -> str:
    return f"Hola {nombre}!"

def main():
    nombre = input("Ingrese su nombre: ").strip()
    if not nombre:
        nombre = "Usuario"
    print(saludar_usuario(nombre))

if __name__ == "__main__":
    main()
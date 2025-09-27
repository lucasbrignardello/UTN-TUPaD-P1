

num1 = int(input("Ingrese el primer número entero distinto de 0: "))
num2 = int(input("Ingrese el segundo número entero distinto de 0: "))

if num1 == 0 or num2 == 0:
    print("Ambos números deben ser distintos de 0.")
else:
    print(f"Suma: {num1 + num2}")
    print(f"Resta: {num1 - num2}")
    print(f"Multiplicación: {num1 * num2}")
    print(f"División: {num1 / num2}")
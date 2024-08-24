# Crear una lista con 10 números enteros
numeros = [10, 23, 44, 57, 92, 31, 18, 99, 0, 75]

# Recorrer la lista utilizando la sentencia for
for num in numeros:
    # Verificar si el número es par, impar o cero
    if num == 0:
        print(f"El número {num} es cero.")
    elif num % 2 == 0:
        print(f"El número {num} es par.")
    else:
        print(f"El número {num} es impar.")
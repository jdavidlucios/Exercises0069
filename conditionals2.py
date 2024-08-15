# Pedir los 3 números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Verificar que los números sean diferentes
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Error: los números deben ser diferentes")
else:
    # Ordenar los números de mayor a menor
    if num1 > num2 and num1 > num3:
        mayor = num1
        if num2 > num3:
            medio = num2
            menor = num3
        else:
            medio = num3
            menor = num2
    elif num2 > num1 and num2 > num3:
        mayor = num2
        if num1 > num3:
            medio = num1
            menor = num3
        else:
            medio = num3
            menor = num1
    else:
        mayor = num3
        if num1 > num2:
            medio = num1
            menor = num2
        else:
            medio = num2
            menor = num1

    # Imprimir el orden de los números
    print("El orden de los números de mayor a menor es:")
    print(f"{mayor}, {medio}, {menor}")
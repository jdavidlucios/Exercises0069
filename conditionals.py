numero = int(input("Ingrese un número: "))

if numero > 0:
    print("El número es positivo")
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
elif numero < 0:
    print("El número es negativo")
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
else:
    print("El número es cero")
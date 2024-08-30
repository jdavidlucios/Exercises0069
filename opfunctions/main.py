from opfunctions import sumar, restar, multiplicar, dividir, operaciones_basicas

def main():
    try:
        # Solicitar al usuario que ingrese dos números
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        # Realizar todas las operaciones y almacenar los resultados en un diccionario
        resultados = {}
        resultados['Suma'] = sumar(num1, num2)
        resultados['Resta'] = restar(num1, num2)
        resultados['Multiplicación'] = multiplicar(num1, num2)
        resultados['División'] = dividir(num1, num2)
        
        # Mostrar los resultados al usuario
        print("\nResultados:")
        for operacion, resultado in resultados.items():
            print(f"{operacion}: {resultado}")
        
        # Preguntar al usuario cuál resultado específico quiere volver a ver
        opcion = input("\n¿Qué operación deseas ver (Suma, Resta, Multiplicación, División)? ").capitalize()

        # Mostrar el resultado correspondiente
        if opcion in resultados:
            print(f"\nEl resultado de la {opcion} es: {resultados[opcion]}")
        else:
            print("\nOperación no reconocida. Por favor, intenta de nuevo.")
        
        # Obtener y mostrar la tupla con todos los resultados numéricos
        suma_result, resta_result, multi_result, div_result = operaciones_basicas(num1, num2)
        print(f"\nResultados de todas las operaciones:")
        print(f"Suma: {suma_result}, Resta: {resta_result}, Multiplicación: {multi_result}, División: {div_result}")

    except ValueError:
        print("Error: Por favor, ingresa números válidos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

if __name__ == "__main__":
    main()

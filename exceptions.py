def main():
    try:
        # Solicitar al usuario que ingrese dos números
        suma = float(input("Introduce el primer número (dividendo): "))
        contador = float(input("Introduce el segundo número (divisor): "))
        
        # Intentar hacer la división
        resultado = suma / contador
        print("El resultado de la división es:", resultado)
    
    # Capturar la excepción si el divisor es cero
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    
    # Capturar la excepción si la entrada no es numérica
    except ValueError:
        print("Error: Por favor, introduce valores numéricos.")

if __name__ == "__main__":
    main()

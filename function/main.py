from rectangle import calcular_area_rectangulo

def main():
    try:
        # Solicitar base y altura al usuario
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        
        # Calcular el área utilizando la función
        area = calcular_area_rectangulo(base, altura)
        
        # Mostrar el resultado
        print(f"El área del rectángulo es: {area}")
    except ValueError as e:
        # Manejar posibles errores y mostrar mensajes al usuario
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
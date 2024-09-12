def main():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero. Intente nuevamente.")

    if edad >= 18:
        print("Usted es un adulto.")
    else:
        print("Usted no es un adulto.")
        
if __name__ == "__main__":
    main()
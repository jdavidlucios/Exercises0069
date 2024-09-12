class RangoSalarioError(Exception):
    def __init__(self, salario):
        self.salario = salario
        self.message = f"{salario} -> Salario no está definido en el rango (1000 a 2000)"
        super().__init__(self.message)  # Llama al constructor de la clase base con el mensaje

def ingresar_salario():
    while True:
        try:
            salario = int(input("Ingrese el salario: "))
            if not 1000 <= salario <= 2000:
                raise RangoSalarioError(salario)
            break  # Sale del bucle si el salario es válido
        except ValueError:
            print("Error: Debe ingresar un número entero. Intente nuevamente.")
        except RangoSalarioError as e:
            print(e)
    
    print("Salario modificado de forma exitosa.")  # Mensaje cuando se ingresa un salario válido

def main():
    print("Programa para ingresar salario")
    ingresar_salario()

if __name__ == "__main__":
    main()

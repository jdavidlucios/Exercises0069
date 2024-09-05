class Animal:
    def __init__(self, nombre, tipo, raza, edad, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.raza = raza
        self.edad = edad
        self.peso = peso

def main():
    # Instancia de objetos de la clase Animal
    caballo = Animal("Zeus", "caballo", "Pura sangre", 5, 450)
    leon = Animal("Boulder", "león", "Atlas", 10, 130)

    # Imprimir información de los animales
    print(f"Animal: {caballo.nombre}, Tipo: {caballo.tipo}, Raza: {caballo.raza}, Edad: {caballo.edad}, Peso: {caballo.peso}kg")
    print(f"Animal: {leon.nombre}, Tipo: {leon.tipo}, Raza: {leon.raza}, Edad: {leon.edad}, Peso: {leon.peso}kg")

if __name__ == "__main__":
    main()

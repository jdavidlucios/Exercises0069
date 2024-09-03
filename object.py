class Animal:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def caminar(self):
        print(f"{self.nombre} está caminando.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

def main():
    # Instancia de objetos de la clase Animal
    perro = Animal("Brando", "San Bernardo", 3, 30)
    gato = Animal("Roll", "Persa", 4, 3)

    # Llama a los métodos de los objetos
    perro.comer()  # Output: Brando está comiendo.
    gato.caminar()  # Output: Roll está caminando.
    perro.dormir()  # Output: Brando está durmiendo.
    gato.comer()  # Output: Roll está comiendo.

# Este bloque se asegura de que main() solo se ejecute si el archivo es ejecutado directamente
if __name__ == "__main__":
    main()

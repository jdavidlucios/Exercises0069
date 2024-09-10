class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def movimiento(self):
        return "caminando"

class Maratonista(Persona):
    def movimiento(self):
        return "trotando"

class Ciclista(Persona):
    def movimiento(self):
        return "rodando"

def main():
    persona = Persona("Juan")
    print(f"{persona.nombre} está {persona.movimiento()}")  # Output: Juan está caminando

    maratonista = Maratonista("María")
    print(f"{maratonista.nombre} está {maratonista.movimiento()}")  # Output: María está trotando

    ciclista = Ciclista("Pedro")
    print(f"{ciclista.nombre} está {ciclista.movimiento()}")  # Output: Pedro está rodando

if __name__ == "__main__":
    main()

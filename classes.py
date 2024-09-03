class Persona:
    def __init__(self, id, nombre, apellidos, edad):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def concentrarse(self):
        print(f"{self.nombre} se está concentrando.")

    def viajar(self):
        print(f"{self.nombre} está viajando.")

class Futbolista(Persona):
    def __init__(self, id, nombre, apellidos, edad, dorsal, demarcacion):
        super().__init__(id, nombre, apellidos, edad)
        self.dorsal = dorsal
        self.demarcacion = demarcacion

    def jugarPartido(self):
        print(f"{self.nombre} está jugando un partido.")

    def entrenar(self):
        print(f"{self.nombre} está entrenando.")

class Entrenador(Persona):
    def __init__(self, id, nombre, apellidos, edad, idFederacion):
        super().__init__(id, nombre, apellidos, edad)
        self.idFederacion = idFederacion

    def dirigirPartido(self):
        print(f"{self.nombre} está dirigiendo un partido.")

    def dirigirEntrenamiento(self):
        print(f"{self.nombre} está dirigiendo un entrenamiento.")

class Masajista(Persona):
    def __init__(self, id, nombre, apellidos, edad, titulacion, annosExperiencia):
        super().__init__(id, nombre, apellidos, edad)
        self.titulacion = titulacion
        self.annosExperiencia = annosExperiencia

    def darMasajes(self):
        print(f"{self.nombre} está dando masajes.")

# Ejemplo de uso
if __name__ == "__main__":
    futbolista = Futbolista(1, "James", "Rodríguez", 34, 10, "Mediocampista")
    entrenador = Entrenador(2, "Pepe", "Guardiola", 53, "1234")
    masajista = Masajista(3, "Carlos", "García", 45, "Diplomado en Fisioterapia", 20)

    futbolista.concentrarse()
    futbolista.jugarPartido()
    entrenador.dirigirPartido()
    masajista.darMasajes()

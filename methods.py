class Persona:
    def __init__(self, nombre, apellido, sexo, edad, estatura, peso):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sexo = sexo
        self.__edad = edad
        self.__estatura = estatura
        self.__peso = peso

    # Métodos get
    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellido

    def get_sexo(self):
        return self.__sexo

    def get_edad(self):
        return self.__edad

    def get_estatura(self):
        return self.__estatura

    def get_peso(self):
        return self.__peso

    # Métodos set
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellidos(self, apellido):
        self.__apellido = apellido

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_edad(self, edad):
        self.__edad = edad

    def set_estatura(self, estatura):
        self.__estatura = estatura

    def set_peso(self, peso):
        self.__peso = peso

    def __str__(self):
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, Sexo: {self.__sexo}, Edad: {self.__edad}, Estatura: {self.__estatura} mts, Peso: {self.__peso} Kg"

def main():
    # Instancia de objetos
    Persona_1 = Persona("Pedro", "Vivas", "Masculino", 20, 1.78, 68)
    Persona_2 = Persona("Juan", "Camargo", "Masculino", 18, 1.8, 75)
    
    # Imprimir información inicial
    print("Persona 1: ")
    print(Persona_1)

    print("\nPersona 2: ")
    print(Persona_2)
    
    Persona_1.set_edad(21)
    Persona_2.set_apellidos("Santiago")

    # Imprimir información actualizada
    print("\nPersona 1 actualizada: ")
    print(Persona_1)

    print("\nPersona 2 actualizada: ")
    print(Persona_2)

if __name__ == "__main__":
    main()

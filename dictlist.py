# Creamos un diccionario para cada persona con sus datos personales
persona1 = {"nombre": "Juan", "apellido": "Pérez", "teléfono": "123456789"}
persona2 = {"nombre": "María", "apellido": "González", "teléfono": "987654321"}
persona3 = {"nombre": "Pedro", "apellido": "Rodríguez", "teléfono": "555123456"}

# Creamos una lista para almacenar los diccionarios de cada persona
registro_personas = [persona1, persona2, persona3]

# Imprimimos la lista de personas en pantalla
print("Registro de personas:")
for i, persona in enumerate(registro_personas):
    print(f"Persona {i+1}:")
    print(f"  Nombre: {persona['nombre']}")
    print(f"  Apellido: {persona['apellido']}")
    print(f"  Teléfono: {persona['teléfono']}")
    print()
def hacer_grandioso(magos):
    """Añade 'El gran' antes del nombre de cada mago"""
    return ["El gran " + mago for mago in magos]

def imprimir_nombres(nombres):
    """Imprime el nombre de cada persona en la lista"""
    for nombre in nombres:
        print(nombre)

# Lista de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Separar los nombres en tres grupos
magos = [nombre for nombre in nombres if nombre in ["Harry Houdini", "David Blaine", "Teller"]]
cientificos = [nombre for nombre in nombres if nombre in ["Newton", "Hawking", "Einstein"]]
otros = [nombre for nombre in nombres if nombre not in magos + cientificos]

# Imprimir la lista completa de nombres antes de ser modificados
print("Lista completa de nombres antes de ser modificados:")
imprimir_nombres(nombres)

# Hacer grandioso a los magos
magos_grandiosos = hacer_grandioso(magos)

# Imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes
print("\nMagos grandiosos:")
imprimir_nombres(magos_grandiosos)
print("\nCientíficos:")
imprimir_nombres(cientificos)
print("\nOtros:")
imprimir_nombres(otros)
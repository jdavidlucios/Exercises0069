estudiantes = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

def es_primo(n):
    """Función para determinar si un número es primo"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Filtra y muestra los estudiantes que tienen más de 18 años y cuyo promedio de calificaciones sea superior a 85
print("Estudiantes con más de 18 años y promedio de calificaciones superior a 85:")
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and sum(estudiante['calificaciones']) / len(estudiante['calificaciones']) > 85:
        print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificaciones: {estudiante['calificaciones']}")

# Calcula el promedio de las calificaciones de los estudiantes que tienen más de 18 años y cuya edad es un número primo
suma_calificaciones = 0
contador = 0
for estudiante in estudiantes:
    if estudiante['edad'] > 18 and es_primo(estudiante['edad']):
        suma_calificaciones += sum(estudiante['calificaciones'])
        contador += len(estudiante['calificaciones'])
if contador > 0:
    promedio_calificaciones = suma_calificaciones / contador
    print(f"\nPromedio de calificaciones de estudiantes con edad primo: {promedio_calificaciones:.2f}")
else:
    print("\nNo hay estudiantes con edad primo.")
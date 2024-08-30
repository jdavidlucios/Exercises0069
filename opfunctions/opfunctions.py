def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def operaciones_basicas(a, b):
    """Realiza operaciones básicas con dos números y devuelve una tupla con los resultados"""
    suma_result = sumar(a, b)
    resta_result = restar(a, b)
    multiplicacion_result = multiplicar(a, b)
    division_result = dividir(a, b)

    # Devolver los resultados como una tupla
    return suma_result, resta_result, multiplicacion_result, division_result

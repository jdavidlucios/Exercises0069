def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dados su base y altura.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.

    Raises:
        ValueError: Si la base o la altura no son números positivos.
    """
    if not (isinstance(base, (int, float)) and isinstance(altura, (int, float))):
        raise ValueError("La base y la altura deben ser números")
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser números positivos")

    return base * altura
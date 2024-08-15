palabra = "paralelepípedo"

vocales = "aeiouí"

consonantes = [(letra, i+1) for i, letra in enumerate(palabra) if letra.lower() not in vocales]

print("Consonantes y su posición:")
for consonante, posicion in consonantes:
    print(f"{consonante} en la posición {posicion}")
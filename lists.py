lista_de_listas = [[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

diccionario = {}

for i, sublista in enumerate(lista_de_listas):
    clave = chr(ord('A') + i)  # Asignar clave A, B, C, D, ...
    diccionario[clave] = sublista

    if sublista[0] != 0:
        print(f"{clave}: ", end="")
        for num in sublista:
            if num != 0:
                print(num, end=" ")
        print()

print("\nDiccionario resultante:")
print(diccionario)
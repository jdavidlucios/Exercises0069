def crear_archivo():
    archivo_nombre = 'informacion.dat'
    try:
        with open(archivo_nombre, 'x') as archivo:
            archivo.write('Datos de información en la línea 1\n')
            archivo.write('Datos de información en la línea 2\n')
            archivo.write('Datos de información en la línea 3\n')
            archivo.write('Datos de información en la línea 4\n')
            archivo.write('Datos de información en la línea 5\n')
        print(f'Archivo {archivo_nombre} creado exitosamente.')
    except FileExistsError:
        print(f'El archivo {archivo_nombre} ya existe.')

def main():
    crear_archivo()

if __name__ == '__main__':
    main()
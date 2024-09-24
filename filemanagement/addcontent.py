import os

def agregar_contenido():
    script_dir = os.path.dirname(__file__)
    archivo_nombre = os.path.join(script_dir, 'informacion.dat')
    try:
        with open(archivo_nombre, 'a') as archivo:
            archivo.write('Hola Mundo\n')
            archivo.write('Esto es una nueva línea en el archivo\n')
            archivo.write('agregando otra línea al archivo\n')
            archivo.write('finalizando con nueva línea agregada\n')
        print(f'Contenido agregado exitosamente al archivo {archivo_nombre}.')
    except FileNotFoundError:
        print(f'El archivo {archivo_nombre} no existe.')

def main():
    agregar_contenido()

if __name__ == '__main__':
    main()
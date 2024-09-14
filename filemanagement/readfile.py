import os

def leer_archivo():
    script_dir = os.path.dirname(__file__)
    archivo_nombre = os.path.join(script_dir, 'informacion.dat')
    try:
        with open(archivo_nombre, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f'El archivo {archivo_nombre} no existe.')

def main():
    leer_archivo()

if __name__ == '__main__':
    main()
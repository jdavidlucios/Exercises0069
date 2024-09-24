import os

def reemplazar_palabra():
    script_dir = os.path.dirname(__file__)
    archivo_nombre = os.path.join(script_dir, 'informacion.dat')
    try:
        # Leer el archivo en modo 'r+' con codificación 'latin-1'
        with open(archivo_nombre, 'r+', encoding='latin-1') as f:
            lineas = f.readlines()  # Leer todas las líneas del archivo
            
            reemplazos = 0
            for i in range(min(5, len(lineas))):  # Limitar el reemplazo a las primeras 5 líneas
                # Usar caracteres corregidos en la palabra a reemplazar
                nuevos_datos, num_reemplazos = lineas[i].replace('informaci�n', 'procesamiento'), lineas[i].count('informaci�n')
                
                # Reemplazar directamente el valor hexadecimal correspondiente al carácter "�" (que es \xf3)
                if num_reemplazos == 0:  # Si no se encuentran coincidencias, buscar la palabra mal codificada
                    nuevos_datos, num_reemplazos = lineas[i].replace('informaci\xf3n', 'procesamiento'), lineas[i].count('informaci\xf3n')
                    
                lineas[i] = nuevos_datos
                reemplazos += num_reemplazos  # Contar cuántos reemplazos se realizaron
                
            f.seek(0)  # Volver al principio del archivo
            f.writelines(lineas)  # Escribir las líneas modificadas en el archivo
            f.truncate()  # Eliminar el contenido sobrante si el archivo es más corto que antes

        print(f"Se realizaron {reemplazos} reemplazos.")
        
    except FileNotFoundError:
        print(f"El archivo '{archivo_nombre}' no se encuentra.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

def main():
    # El archivo por defecto es "informacion.dat"
    reemplazar_palabra()

if __name__ == "__main__":
    main()

"""
Leer un archivo de texto con un conjunto de líneas de texto, a
continuación, indicar por pantalla la cantidad de palabras que
comienzan con vocales y la cantidad de palabras de terminan con
consonantes.
"""

def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        palabras = file.read().split()
    return palabras
    
def empieza_con_vocal(palabra):
    return palabra[0].lower() in "aeiou"

def termina_con_consonante(palabra):
    return palabra[-1].lower() in "bcdfghjklmnñpqrstvwxyz"

if __name__ == "__main__":
    archivo = "archivo.txt"
    palabras = leer_archivo(archivo)
    contador_vocales = 0
    contador_consonantes = 0
    for palabra in palabras:
        if empieza_con_vocal(palabra):
            contador_vocales += 1
        if termina_con_consonante(palabra):
            contador_consonantes += 1
    print(f"Palabras que comienzan con vocales: {contador_vocales}")
    print(f"Palabras que terminan con consonantes: {contador_consonantes}")

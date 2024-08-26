"""
Funcion para leer dos cadenas de texto
primera linea: frase a adivinar
segunda linea: vidas del jugador
"""

def leer_archivo(archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()
    return lineas

def ahorcado(archivo):
    lineas = leer_archivo(archivo)
    frase = lineas[0].strip()
    vidas = int(lineas[1])
    letras_frase = set(frase)
    letras_adivinadas = set()
    letras_falladas = set()
    while vidas > 0 and letras_frase != letras_adivinadas:
        print("Vidas restantes:", vidas)
        print("Frase:", " ".join(letra if letra in letras_adivinadas else "_" for letra in frase))
        letra = input("Introduce una letra: ")
        if letra in letras_frase:
            letras_adivinadas.add(letra)
        else:
            letras_falladas.add(letra)
            vidas -= 1
    if letras_frase == letras_adivinadas:
        print("¡Has adivinado la frase!")
    else:
        print("¡Has perdido!")
    print("Letras adivinadas:", " ".join(letras_adivinadas))
    print("Letras falladas:", " ".join(letras_falladas))

if __name__ == "__main__":
    ahorcado("09_ahorcado.txt")
"""
● Realice un programa que lea tantas cadenas de String como el usuario
indique por teclado, a continuación, para cada cadena separe cada
palabra por espacio (“ ”) y muestre en pantalla dos mensajes:
○ El primero contiene todas las palabras que ocupan una posición
impar en el texto.
○ El segundo contiene todas las palabras que ocupan una posición par
en el texto.
● Ejemplo: “Hugo y Philip somos sus profes”
○ Mensaje 1: “Hugo Philip sus”
○ Mensaje 2: “y somos profes”

"""


def procesar_cadena(cadena):
    palabras = cadena.split()
    print(f"Son las palabras: {palabras}")
    impares = " ".join(palabras[::2]) # palabras en posiciones impares [inicio:final:salto]
    print(f"{impares}")
    pares = " ".join(palabras[1::2])
    print(f"{pares}")
    return impares, pares

# Pedir al usuario el número de cadenas
num_cadenas = int(input("Ingrese el número de cadenas que desea procesar: "))

for i in range(num_cadenas):
    # Leer la cadena del usuario
    cadena = input(f"\nIngrese la cadena #{i+1}: ")
    
    # Procesar la cadena
    impares, pares = procesar_cadena(cadena)
    
    # Mostrar resultados
    print(f"\nPara la cadena: '{cadena}'")
    print(f"Mensaje 1 (palabras en posiciones impares): '{impares}'")
    print(f"Mensaje 2 (palabras en posiciones pares): '{pares}'")
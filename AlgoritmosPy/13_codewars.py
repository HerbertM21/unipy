"""
Se te dará una palabra. Tu trabajo es devolver el carácter medio de la palabra. Si la longitud de la palabra es extraña, devuelve el carácter medio. Si la longitud de la palabra es uniforme, devuelva los 2 caracteres medios.

#Ejemplos:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
#Input

Una palabra (cadena) de longitud 0 < str < 1000 (En javascript puede obtener un poco más de 1000 en algunos casos de prueba debido a un error en los casos de prueba). No necesita probar esto. Esto solo está aquí para decirle que no necesita preocuparse por el tiempo de espera de su solución.

#Salida

El carácter medio(s) de la palabra representada como una cadena.
"""


palabra = "testing"

if len(palabra) % 2 == 0: # Par
    print(palabra[len(palabra) // 2 - 1:len(palabra) // 2 + 1])
else: # Impar
    print(palabra[len(palabra) // 2])
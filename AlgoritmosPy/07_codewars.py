"""

● Realizar un programa donde se solicite una cadena al usuario, a
continuación, el programa imprimirá la cadena invertida caracter a
caracter y una cadena invertida en grupos de 4 caracteres.
● Ejemplo:
    ○ Entrada: “Ingeniería en la UCM”
    ○ Salida: “ MCU al ne aíreinegnI”
    “ UCMn laía enierInge”

"""

# Solicitar una cadena al usuario
cadena = input("Introduce una cadena: ")

# Invertir la cadena carácter por carácter
cadena_invertida = ''.join(reversed(cadena))
print("Cadena invertida carácter por carácter:", cadena_invertida)

# Invertir la cadena en grupos de 4 caracteres
cadena_invertida_grupo = ''.join(reversed([cadena[i:i+4] for i in range(0, len(cadena), 4)]))
print("Cadena invertida en grupos de 4 caracteres:", cadena_invertida_grupo)

"""
Lista por comprensión: [cadena[i:i+4] for i in range(0, len(cadena), 4)]

La cadena tiene 20 caracteres.
range(0, 20, 4) genera los índices 0, 4, 8, 12, 16.
Resultado: ["Inge", "nier", "ia e", "n la", " UCM"]


reversed()

Invierte el orden de los grupos:
Resultado: [" UCM", "n la", "ia e", "nier", "Inge"]


''.join()

Une todos los grupos invertidos en una sola cadena:
Resultado final: " UCMn laia enier Inge"
"""
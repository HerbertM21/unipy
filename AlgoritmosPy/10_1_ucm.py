"""
Emilia es una niña con suerte, su abuela Ximena es propietaria de una parcela. 
Emilia le pide frutos secos (pistachos, maníes, nueces, etc), pero su sabia abuelita le permite comer 
cantidades limitadas para cuidar de su salud. Ximena es aficionada a los números binarios, 
así que le propone el siguiente juego: la abuelita dirá un número N, y Emilia escogería dos números (x e y),
tales que la suma de ambos debe dar N. Entonces, Ximena daría a Emilia tantos frutos secos como la cantidad 
de unos que tengan x e y en base 2. Por ejemplo, si Ximena propone 7 y Emilia escoge 3 y 4, 
recibiría 3 frutitas (3 es (11)2 y 4 es (100)2 ). 
Emilia quisiera saber la máxima cantidad de frutitas que podría obtener de Ximena. 
La entrada del programa será un número N, la salida será una lista de todos los posibles casos que 
cumplen con las restricciones descritas, seguida del caso donde Emilia recibe más frutos secos
"""

def contar_unos(n):
    return bin(n).count('1')

def resolver_problema_frutos(N):
    max_frutos = contar_unos(N)
    return max_frutos

# Ejemplo de uso
N = int(input("Ingrese el número N propuesto por Ximena: "))
max_frutos = resolver_problema_frutos(N)

print(f"Para N = {N}, el máximo número de frutos es: {max_frutos}")
print(f"Esto se puede lograr con cualquier combinación de x e y que sumen {N}")
print(f"Por ejemplo, x = 1, y = {N-1}")
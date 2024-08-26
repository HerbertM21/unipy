"""
Se le da una matriz (que tendrá una longitud de al menos 3, pero podría ser muy grande) que contiene enteros. La matriz está completamente compuesta de enteros impares o completamente compuesta de enteros pares, excepto por un solo entero N. Escriba un método que tome la matriz como un argumento y devuelva este "autlier" N.

Ejemplos
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

"""

def find_outlier(integers):
    pares = []
    impares = []
    for i in integers:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares[0] if len(pares) == 1 else impares[0]


def find_outlier2(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

# Ejemplo de uso

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])) # 11
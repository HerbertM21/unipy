"""
Dadas dos matrices de cuerdas a1 y a2 devuelve una matriz ordenada r en orden lexicográfico de las cuerdas de a1 que son subcadenas de cadenas de a2.

Ejemplo 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

devoluciones ["arp", "live", "strong"]

Ejemplo 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

devoluciones []
"""

# LOS DOS BUSCAN SUBCADENAS EN CADA ELEMENTO DE a2
def method1(a1, a2):
    r = set()
    for x in a1:
        for y in range(len(a2)):
            if x in a2[y]:
                r.add(x)
                break  # Añadimos esto para evitar duplicados
    return sorted(list(r))

def method2(a1, a2):
    r = set()
    for x in a1:
        if any(x in y for y in a2):
            r.add(x)
    return sorted(list(r))

a1 = ["cat", "dog", "bird"]
a2 = ["concatenate", "doghouse", "flying"]

print("Method 1:", method1(a1, a2))
print("Method 2:", method2(a1, a2))
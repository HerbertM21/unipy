def raiz_cuadrada(n, precision=0.0001):
    x = n
    while True:
        raiz = 0.5 * (x + (n / x))
        if abs(raiz - x) < precision:
            return raiz
        x = raiz

# Ejemplo de uso
numero = 16
resultado = raiz_cuadrada(numero)
print(f"La raíz cuadrada de {numero} es aproximadamente {resultado}")
# Numeros primos

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generar_primos(limite):
    return [num for num in range(2, limite + 1) if es_primo(num)]

# Ejemplo de uso
primos = generar_primos(50)
print(primos)
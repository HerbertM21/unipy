def es_narcisista(num):
    str_num = str(num)
    n = len(str_num)
    return sum(int(digit)**n for digit in str_num) == num

def encontrar_narcisistas(limite):
    return [num for num in range(1, limite + 1) if es_narcisista(num)]

# Ejemplo de uso
limite = 1000
numeros_narcisistas = encontrar_narcisistas(limite)
print(f"Números narcisistas hasta {limite}: {numeros_narcisistas}")
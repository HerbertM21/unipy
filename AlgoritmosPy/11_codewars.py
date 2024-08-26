"""
Sumar dos números enteros y devolver el resultado en binario.
"""

def add_binary(a, b):
    return bin(a + b)[2:]

if __name__ == "__main__":
    a = 1
    b = 1
    print(add_binary(a, b)) # 10
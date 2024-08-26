"""
Hacer un algoritmo que lea un número menor que 1000:
○ Si el número tiene un dígito, deberá elevarlo al cuadrado y mostrar
su resultado.
○ Si el número es de dos dígitos, multiplicarlo por dos y mostrar su
resultado.
○ Si el número es de tres dígitos, restarle cien y mostrar el resultado.
○ En otro caso, mostrar la leyenda “Número no válido”.
"""

def number_operation(number):
    if number < 10:
        return number ** 2
    elif number < 100:
        return number * 2
    elif number < 1000:
        return number - 100
    else:
        return "Número no válido"
    
if __name__ == "__main__":
    print(number_operation(5)) # 25
    print(number_operation(15)) # 30
    print(number_operation(150)) # 50
    print(number_operation(1500)) # Número no válido
    print(number_operation(1000)) # Número no válido
    print(number_operation(100)) # 0
    print(number_operation(10)) # 20
    print(number_operation(1)) # 1
    print(number_operation(0)) # 0
    print(number_operation(-1)) # 1
    print(number_operation(-10)) # 20

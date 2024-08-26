"""
Las máquinas ATM permiten códigos PIN de 4 o 6 dígitos y los códigos PIN no pueden contener nada más que exactamente 4 Dígitos o exactamente 6 dígitos.

Si se pasa la función a una cadena PIN válida, devuelva true, de lo contrario volver false.

Ejemplos (Entrada --> Salida)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

if __name__ == "__main__":
    print(validate_pin("1234")) # True
    print(validate_pin("12345")) # False
    print(validate_pin("a234")) # False
    print(validate_pin("123456")) # True
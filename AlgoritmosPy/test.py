string = "Hola Mundo"

for i in range(len(string)):
    # Verificar si cada caracter es digito con is digit
    if string[i].isdigit():
        print(f"El caracter {string[i]} es un dígito")
    else:
        print(f"El caracter {string[i]} no es un dígito")


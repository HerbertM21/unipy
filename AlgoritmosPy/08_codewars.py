def printer_error(s):
    # Definir el conjunto de caracteres válidos
    colores_validos = set('abcdefghijklm')
    
    # Contar el número de errores
    errores = sum(1 for char in s if char not in colores_validos)
    
    # Calcular la longitud de la cadena de control
    longitud_total = len(s)
    
    # Devolver la tasa de errores en el formato "numerador/denominador"
    return f"{errores}/{longitud_total}"

def printer_error2(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))

if __name__ == "__main__":

    # Ejemplos de uso de la función
    print(printer_error("aaabbbbhaijjjm"))
    # Devuelve: "0/14"

    print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))
    # Devuelve: "8/22"

    print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
    # Devuelve: "3/56"
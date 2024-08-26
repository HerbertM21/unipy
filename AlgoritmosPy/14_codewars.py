"""
Crea una función tomando un número entero positivo entre 1 y 3999 (ambos incluidos) como parámetro y devolviendo una cadena que contiene la representación Numeral Romana de ese número entero.

Los números romanos modernos se escriben expresando cada dígito por separado comenzando con el dígito más a la izquierda y omitiendo cualquier dígito con un valor de cero. No puede haber más de 3 símbolos idénticos seguidos.

En números romanos:

1990 se representa: 1000=M + 900=CM + 90=XC; resultando en MCMXC.
2008 está escrito como 2000=MM, 8=VIII; o MMVIII.
1666 utiliza cada símbolo romano en orden descendente: MDCLXVI.
Ejemplo:

   1 -->       "I"
1000 -->       "M"
1666 --> "MDCLXVI"
Ayuda:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000


"""

def to_roman(n):
    roman_numerals = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    result = ""
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while n >= value:
            result += numeral
            n -= value
    return result

if __name__ == "__main__":
    print(sorted({1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}.items(), reverse=True))
    print(to_roman(1)) # I
    print(to_roman(1000)) # M
    print(to_roman(1666)) # MDCLXVI
    print(to_roman(1990)) # MCMXC
    print(to_roman(2008)) # MM
    print(to_roman(499)) 
"""
Cree una función que devuelva la suma de los dos números positivos más bajos dado un array de mínimo 4 enteros positivos. No se pasarán flotadores ni enteros no positivos.
Por ejemplo, cuando se pasa una matriz como [19, 5, 42, 2, 77], la salida debe ser 7.

[10, 343445353, 3453445, 3453545353453] debería volver 3453455.
"""

def sum_two_smallest_numbers(numbers):
    # Ordenamos la lista de menor a mayor
    sorted_numbers = sorted(numbers)
    
    # Sumamos los dos primeros números (que serán los más pequeños)
    return sorted_numbers[0] + sorted_numbers[1]

if __name__ == "__main__":
    print(sum_two_smallest_numbers([19, 5, 42, 2, 77])) # 7
    print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])) # 3453455

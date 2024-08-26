"""
Implementa la función unique_in_order que toma como argumento una secuencia y devuelve una lista de elementos sin ningún elemento con el mismo valor uno al lado del otro y preservando el orden original de los elementos.
Por ejemplo:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""

def unique_in_order1(iterable):
    if len(iterable) == 0:
        return []
    else:
        result = [iterable[0]]
        for i in range(1, len(iterable)):
            if iterable[i] != iterable[i-1]:
                result.append(iterable[i])
        return result
    
def unique_in_order2(iterable):
    result = []
    prev = None
    for item in iterable:
        if item != prev:
            result.append(item)
            prev = item
    return result

if __name__ == "__main__":
    print(unique_in_order1('AAAABBBCCDAABBB')) # ['A', 'B', 'C', 'D', 'A', 'B']
    print(unique_in_order1('ABBCcAD'))         # ['A', 'B', 'C', 'c', 'A', 'D']
    print(unique_in_order1([1, 2, 2, 3, 3]))   # [1, 2, 3]
    print(unique_in_order1((1, 2, 2, 3, 3)) )  # [1, 2, 3]
    print(unique_in_order2('AAAABBBCCDAABBB')) # ['A', 'B', 'C', 'D', 'A', 'B']
    print(unique_in_order2('ABBCcAD'))         # ['A', 'B', 'C', 'c', 'A', 'D']
    print(unique_in_order2([1, 2, 2, 3, 3]))   # [1, 2, 3]
    print(unique_in_order2((1, 2, 2, 3, 3)) )  # [1, 2, 3]
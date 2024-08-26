"""

Esta vez queremos escribir cálculos usando funciones y obtener los resultados. Echemos un vistazo a algunos ejemplos:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requisitos:
* Debe haber una función para cada número de 0 ("cero") a 9 ("nueve")
* Debe haber una función para cada una de las siguientes operaciones matemáticas: más, menos, veces, dividido_by
* Cada cálculo consiste exactamente en una operación y dos números
* La función más externa representa el operando izquierdo, la función más interna representa el operando derecho
* La división debería ser división entera. Por ejemplo, esto debería volver 2, no 2.666666...:


eight(divided_by(three()))

"""


def zero(func=None): return func(0) if func else 0
def one(func=None): return func(1) if func else 1
def two(func=None): return func(2) if func else 2
def three(func=None): return func(3) if func else 3
def four(func=None): return func(4) if func else 4
def five(func=None): return func(5) if func else 5
def six(func=None): return func(6) if func else 6
def seven(func=None): return func(7) if func else 7
def eight(func=None): return func(8) if func else 8
def nine(func=None): return func(9) if func else 9

def plus(y):
    return lambda x: x + y

def minus(y):
    return lambda x: x - y

def times(y):
    return lambda x: x * y

def divided_by(y):
    return lambda x: x // y

# Ejemplos de uso
print(seven(times(five())))  # 35
print(four(plus(nine())))    # 13
print(eight(minus(three()))) # 5
print(six(divided_by(two())))# 3
print(eight(divided_by(three()))) # 2
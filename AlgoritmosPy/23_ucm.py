# Factorial (iterativo)
def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Factorial (recursivo)
def factorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

# Fibonacci (iterativo)
def fibonacci_iterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Fibonacci (recursivo)
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Coeficiente binomial
def coeficiente_binomial(n, k):
    return factorial_iterativo(n) // (factorial_iterativo(k) * factorial_iterativo(n - k))

# Conjetura de Collatz
def collatz(n):
    secuencia = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        secuencia.append(n)
    return secuencia

# Ejemplos de uso
if __name__ == "__main__":
    print("Factorial (iterativo) de 5:", factorial_iterativo(5))
    print("Factorial (recursivo) de 5:", factorial_recursivo(5))
    print("Fibonacci (iterativo) de 10:", fibonacci_iterativo(10))
    print("Fibonacci (recursivo) de 10:", fibonacci_recursivo(10))
    print("Coeficiente binomial de 5 sobre 2:", coeficiente_binomial(5, 2))
    print("Secuencia de Collatz para 6:", collatz(6))
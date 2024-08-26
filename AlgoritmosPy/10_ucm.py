def contar_unos(n):
    return bin(n).count('1')

def resolver_problema_frutos(N):
    resultados = []
    max_frutos = 0
    mejor_caso = None

    for x in range(1, N):
        y = N - x
        frutos = contar_unos(x) + contar_unos(y)
        resultados.append((x, y, frutos))
        
        if frutos > max_frutos:
            max_frutos = frutos
            mejor_caso = (x, y, frutos)

    return resultados, mejor_caso

if __name__ == "__main__":
    N = int(input("Ingrese el número N propuesto por Ximena: "))
    todos_casos, mejor_caso = resolver_problema_frutos(N)

    print("Todos los casos posibles:")
    for caso in todos_casos:
        print(f"x = {caso[0]}, y = {caso[1]}, frutos = {caso[2]}")

    print("\nCaso donde Emilia recibe más frutos secos:")
    print(f"x = {mejor_caso[0]}, y = {mejor_caso[1]}, máximo de frutos = {mejor_caso[2]}")
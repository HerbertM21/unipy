def es_pangrama(frase):
    # Definir el conjunto de letras del alfabeto inglés
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    
    # Convertir la frase a minúsculas y crear un conjunto con sus letras
    letras_frase = set(frase.lower())
    
    # Verificar si todas las letras del alfabeto están en la frase
    return alfabeto.issubset(letras_frase)

if __name__ == "__main__":
    frases = [
    "The quick brown fox jumps over the lazy dog",
    "El veloz murciélago hindú comía feliz cardillo y kiwi",
    "Una frase que no es un pangrama"
    ]

    for frase in frases:
        if es_pangrama(frase):
            print(f"La frase '{frase}' es un pangrama")
        else:
            print(f"La frase '{frase}' no es un pangrama")
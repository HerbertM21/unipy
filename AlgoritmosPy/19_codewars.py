"""
El equipo de marketing pasa demasiado tiempo escribiendo hashtags.
¡Ayudémoslos con nuestro propio Generador Hashtag!

Aquí está el trato:

Debe comenzar con un hashtag (#).
Todas las palabras deben tener su primera letra en mayúscula.
Si el resultado final es superior a 140 caracteres, debe devolver false.
Si la entrada o el resultado es una cadena vacía, debe volver false.
Ejemplos
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""

def generator_hashtag(string):
    palabras = [x[0].upper()+(x[1:len(x)]).lower() for x in string.split()]
    resultado = "#"
    
    for x in palabras:
        resultado += x
    return False if len(resultado) == 1 or len(resultado) > 140 else resultado


#print(generator_hashtag("Hello there thanks for trying my Kata"))

# va a haber un problema si la frase no es capitalize o lower
# por lo tanto, se debe convertir en lower todas las palabras o simplemente un capitalize
print(generator_hashtag("CoDeWaRs is niCe")) 

"""

string = "CoDeWaRs is niCe"
print([x[0].upper()+x[1:len(x)] for x in string.split()])
print((string.replace(" ", "")))
"""
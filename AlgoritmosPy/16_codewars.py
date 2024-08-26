"""
Vives en la ciudad de Cartesia, donde todos los caminos están dispuestos en una cuadrícula perfecta. Llegaste diez minutos demasiado temprano para una cita, así que decidiste aprovechar la oportunidad para dar un corto paseo. La ciudad proporciona a sus ciudadanos una aplicación Walk Generating en sus teléfonos: cada vez que presiona el botón, le envía una serie de cadenas de una letra que representan instrucciones para caminar (por ejemplo, ['n', 's', 'w', 'e']). Siempre caminas solo un bloque por cada letra (dirección) y sabes que te lleva un minuto atravesar una cuadra de ciudad, así que crea una función que volverá cierto si la caminata que te da la aplicación te llevará exactamente diez minutos (¡no quieres llegar temprano o tarde!) y, por supuesto, lo devolverá a su punto de partida. Devolución falso de lo contrario.

Nota: siempre recibirá una matriz válida que contiene una variedad aleatoria de letras de dirección ('n', 's', 'e' o 'w' solamente). Nunca te dará una matriz vacía (eso no es una caminata, ¡eso está parado!).
                                                                                                                                                                     
"""  

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    return walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e')

# Ejemplo de uso

print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'])) # False
"""
Escribe una función que cuando se le da una URL como una cadena, analiza solo el nombre de dominio y lo devuelve como una cadena. Por ejemplo:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def dominio(string):
    # Eliminar el protocolo si existe
    if "://" in url:
        url = url.split("://")[1]
    
    # Eliminar la ruta y los parámetros si existen
    url = url.split('/')[0]
    
    # Eliminar 'www.' si está presente
    if url.startswith('www.'):
        url = url[4:]
    
    # Dividir por '.' y tomar la primera parte
    partes = url.split('.')
    
    # Manejar casos especiales como 'co.uk'
    dominios_especiales = ['co', 'com', 'org', 'net', 'edu', 'gov']
    if len(partes) > 2 and partes[-2] in dominios_especiales:
        return partes[-3]
    
    return partes[0]


string = "hola.com"
print(dominio("http://www.zombie-bites.com"))



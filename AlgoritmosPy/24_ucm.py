def corregir_mensaje(mensaje_erroneo):
    # Paso 1: Reemplazar comas por espacios
    mensaje_intermedio = mensaje_erroneo.replace(',', ' ')
    
    # Paso 2: Reemplazar '#' por comas
    mensaje_corregido = mensaje_intermedio.replace('#', ',')
    
    return mensaje_corregido

# Ejemplo de uso
mensaje_erroneo = "La,cantimplora,se,calentó#tomar,agua,así,no,tiene,gracia"
mensaje_corregido = corregir_mensaje(mensaje_erroneo)

print("Mensaje original:", mensaje_erroneo)
print("Mensaje corregido:", mensaje_corregido)
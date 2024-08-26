"""
Su tarea para completar este Kata es escribir una función que formatee una duración, dada como un número de segundos, de una manera amigable para los humanos.

La función debe aceptar un número entero no negativo. Si es cero, solo regresa "now". De lo contrario, la duración se expresa como una combinación de years, days, hours, minutes y seconds.

Es mucho más fácil de entender con un ejemplo:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
Para el propósito de este Kata, un año es de 365 días y un día es de 24 horas.

Tenga en cuenta que los espacios son importantes.

Reglas detalladas
La expresión resultante está hecha de componentes como 4 seconds, 1 year, etc. En general, un número entero positivo y una de las unidades de tiempo válidas, separadas por un espacio. La unidad de tiempo se usa en plural si el número entero es mayor que 1.

Los componentes están separados por una coma y un espacio (", "). Excepto el último componente, que está separado por " and ", al igual que estaría escrito en inglés.

Se producirán unidades de tiempo más significativas antes que una menos significativa. Por lo tanto, 1 second and 1 year no es correcto, pero 1 year and 1 second es.

Diferentes componentes tienen diferentes unidades de tiempo. Así que no hay unidades repetidas como en 5 seconds and 1 second.

Un componente no aparecerá en absoluto si su valor es cero. Por lo tanto, 1 minute and 0 seconds no es válido, pero debería ser justo 1 minute.

Se debe usar una unidad de tiempo "tanto como sea posible". Significa que la función no debe volver 61 seconds, pero 1 minute and 1 second en cambio. Formalmente, la duración especificada por un componente no debe ser mayor que cualquier unidad de tiempo válida más significativa.
"""

def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        years = seconds // 31536000
        days = (seconds % 31536000) // 86400
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        
        time = []
        if years > 0:
            time.append(f"{years} year" if years == 1 else f"{years} years")
        if days > 0:
            time.append(f"{days} day" if days == 1 else f"{days} days")
        if hours > 0:
            time.append(f"{hours} hour" if hours == 1 else f"{hours} hours")
        if minutes > 0:
            time.append(f"{minutes} minute" if minutes == 1 else f"{minutes} minutes")
        if seconds > 0:
            time.append(f"{seconds} second" if seconds == 1 else f"{seconds} seconds")
        
        if len(time) == 1:
            return time[0]
        elif len(time) == 2:
            return f"{time[0]} and {time[1]}"
        else:
            return ", ".join(time[:-1]) + " and " + time[-1]
        
# Ejemplos de uso
print(format_duration(1)) # 1 second
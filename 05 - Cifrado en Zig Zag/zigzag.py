def cifrado_zigzag(texto, num_filas):
    if num_filas == 1:
        return texto  # Si hay solo una fila, el texto no cambia

    # Inicializar las filas vacías
    filas = ['' for _ in range(num_filas)]
    
    # Usar una bandera para determinar la dirección 
    # (sube o baja por las filas)
    bajar = False
    fila_actual = 0
    
    # Iterar sobre cada caracter en el texto
    for caracter in texto:
        # Añadir el caracter a la fila actual
        filas[fila_actual] += caracter
        
        # Si llegamos al fondo o la cima, cambiar de dirección
        if fila_actual == 0 or fila_actual == num_filas - 1:
            bajar = not bajar
        
        # Mover hacia arriba o abajo
        fila_actual += 1 if bajar else -1
    
    # Combinar todas las filas en el texto cifrado
    return ''.join(filas)

def descifrar_zigzag(texto_cifrado, num_filas):
    if num_filas == 1:
        return texto_cifrado  # Si hay solo una fila, el texto no cambia

    # Determinar la longitud de cada fila
    longitudes = [0] * num_filas
    bajar = False
    fila_actual = 0
    
    # Primer pase: contar cuántos caracteres van en cada fila
    for _ in texto_cifrado:
        longitudes[fila_actual] += 1
        if fila_actual == 0 or fila_actual == num_filas - 1:
            bajar = not bajar
        fila_actual += 1 if bajar else -1
    
    # Segundo pase: separar el texto cifrado en las filas
    filas = []
    indice = 0
    for longitud in longitudes:
        filas.append(texto_cifrado[indice:indice + longitud])
        indice += longitud
    
    # Ahora reconstruimos el texto original
    resultado = []
    bajar = False
    fila_actual = 0
    indices_filas = [0] * num_filas  # Para mantener el índice de cada fila

    for _ in texto_cifrado:
        # Añadir el siguiente carácter de la fila correspondiente
        resultado.append(filas[fila_actual][indices_filas[fila_actual]])
        indices_filas[fila_actual] += 1
        
        # Cambiar de dirección en la parte superior e inferior
        if fila_actual == 0 or fila_actual == num_filas - 1:
            bajar = not bajar
        
        fila_actual += 1 if bajar else -1
    
    return ''.join(resultado)

# Alfabeto base usado en los ejemplos anteriores
alfabeto_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'

# Ejemplo de uso
texto = "ESTE ES UN MENSAJE"
num_filas = 3

# Cifrar el texto
texto_cifrado = cifrado_zigzag(texto, num_filas)
print(f"Texto cifrado: {texto_cifrado}")

# Descifrar el texto
texto_descifrado = descifrar_zigzag(texto_cifrado, num_filas)
print(f"Texto descifrado: {texto_descifrado}")

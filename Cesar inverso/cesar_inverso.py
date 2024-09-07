def cifrado_inverso_cesar(texto, desplazamiento, tarea):
    # Definir el alfabeto
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'
    resultado = ''
    
    # Ajustar desplazamiento si es descifrado
    if tarea.upper() == 'D':
        desplazamiento = desplazamiento
    else:
        # Si es cifrado, invertimos el desplazamiento para ir hacia atrás
        desplazamiento = -desplazamiento
    
    # Procesar cada caracter en el texto
    for caracter in texto:
        if caracter in alfabeto:
            # Encontrar la posición actual del carácter en el alfabeto
            indice_actual = alfabeto.index(caracter)
            # Calcular la nueva posición con el desplazamiento inverso
            nuevo_indice = (indice_actual + desplazamiento) % len(alfabeto)
            # Añadir el nuevo carácter al resultado
            resultado += alfabeto[nuevo_indice]
        else:
            # Si el carácter no está en el alfabeto, se deja igual
            resultado += caracter
    
    return resultado

# Pedir el desplazamiento al usuario
desplazamiento = int(input("Introduce el desplazamiento: "))

# Pedir si se va a cifrar o descifrar
tarea = input("Introduce 'C' para cifrar o 'D' para descifrar: ").strip().upper()

# Pedir el texto a procesar
texto = input("Introduce el texto a procesar: ")

# Procesar el texto
resultado = cifrado_inverso_cesar(texto, desplazamiento, tarea)

# Mostrar el resultado
print("Texto procesado:", resultado)

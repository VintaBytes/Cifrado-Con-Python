def generar_alfabeto_mezclado(palabra_clave):
    # Definir el alfabeto base
    alfabeto_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'
    
    # Eliminar letras repetidas en la palabra clave y mantener el orden original
    palabra_clave = ''.join(sorted(set(palabra_clave), key=palabra_clave.index))
    
    # Crear el alfabeto cifrado a partir de la palabra clave y las letras restantes del alfabeto
    alfabeto_cifrado = palabra_clave + ''.join([letra for letra in alfabeto_base if letra not in palabra_clave])
    
    return alfabeto_cifrado

def cifrado_mezcla_palabra_clave(texto, palabra_clave, tarea):
    # Generar el alfabeto cifrado basado en la palabra clave
    alfabeto_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'
    alfabeto_cifrado = generar_alfabeto_mezclado(palabra_clave)
    
    resultado = ''
    
    # Procesar cada caracter en el texto
    for caracter in texto:
        if tarea.upper() == 'C':  # Cifrar
            if caracter in alfabeto_base:
                indice = alfabeto_base.index(caracter)
                resultado += alfabeto_cifrado[indice]
            else:
                resultado += caracter  # Si no es un caracter del alfabeto, se deja igual
        elif tarea.upper() == 'D':  # Descifrar
            if caracter in alfabeto_cifrado:
                indice = alfabeto_cifrado.index(caracter)
                resultado += alfabeto_base[indice]
            else:
                resultado += caracter  # Si no es un caracter del alfabeto, se deja igual
    
    return resultado

# Pedir la palabra clave al usuario
palabra_clave = input("Introduce la palabra clave: ")

# Pedir si se va a cifrar o descifrar
tarea = input("Introduce 'C' para cifrar o 'D' para descifrar: ").strip().upper()

# Pedir el texto a procesar
texto = input("Introduce el texto a procesar: ")

# Procesar el texto
resultado = cifrado_mezcla_palabra_clave(texto, palabra_clave, tarea)

# Mostrar el resultado
print("Texto procesado:", resultado)

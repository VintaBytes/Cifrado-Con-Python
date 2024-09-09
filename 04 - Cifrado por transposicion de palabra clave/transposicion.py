def generar_alfabeto_transposicion(palabra_clave):
    # Definir el alfabeto base
    alfabeto_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'
    
    # Eliminar letras repetidas de la palabra clave
    palabra_clave = ''.join(sorted(set(palabra_clave), key=palabra_clave.index))
    
    # Crear la cuadrícula con la palabra clave en la primera fila y las letras restantes del alfabeto
    letras_faltantes = ''.join([letra for letra in alfabeto_base if letra not in palabra_clave])
    
    # Llenar la cuadrícula
    cuadrícula = []
    fila_actual = list(palabra_clave)
    cuadrícula.append(fila_actual)  # Agregar la palabra clave como la primera fila
    
    for i in range(0, len(letras_faltantes), len(fila_actual)):
        cuadrícula.append(list(letras_faltantes[i:i+len(fila_actual)]))
    
    # Generar el alfabeto cifrado leyendo por columnas
    alfabeto_cifrado = ''
    for col in range(len(fila_actual)):
        for fila in cuadrícula:
            if col < len(fila):
                alfabeto_cifrado += fila[col]
    
    return alfabeto_cifrado

def cifrado_transposicion_palabra_clave(texto, palabra_clave, tarea):
    # Generar el alfabeto cifrado basado en la transposición de palabra clave
    alfabeto_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'
    alfabeto_cifrado = generar_alfabeto_transposicion(palabra_clave)
    
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
resultado = cifrado_transposicion_palabra_clave(texto, palabra_clave, tarea)

# Mostrar el resultado
print("Texto procesado:", resultado)

def cifrar_bloques(texto, tamano_bloque):
    # Rellenar el texto con espacios si no es múltiplo del tamaño del bloque
    while len(texto) % tamano_bloque != 0:
        texto += ' '

    # Dividir el texto en bloques de tamaño fijo
    bloques = [texto[i:i + tamano_bloque] for i in range(0, len(texto), tamano_bloque)]

    # Invertir las letras dentro de cada bloque (puedes cambiar la regla de transposición aquí)
    bloques_cifrados = [bloque[::-1] for bloque in bloques]

    # Unir los bloques cifrados en una cadena
    texto_cifrado = ''.join(bloques_cifrados)

    return texto_cifrado

def descifrar_bloques(texto_cifrado, tamano_bloque):
    # Dividir el texto cifrado en bloques del tamaño especificado
    bloques = [texto_cifrado[i:i + tamano_bloque] for i in range(0, len(texto_cifrado), tamano_bloque)]

    # Invertir las letras dentro de cada bloque para descifrar
    bloques_descifrados = [bloque[::-1] for bloque in bloques]

    # Unir los bloques descifrados en una cadena
    texto_descifrado = ''.join(bloques_descifrados)

    return texto_descifrado

# Alfabeto base usado en los ejemplos anteriores
alfabeto_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'

# Pedir al usuario el texto a procesar
texto = input("Introduce el texto: ")

# Pedir al usuario el tamaño del bloque
tamano_bloque = int(input("Introduce el tamaño del bloque: "))

# Pedir al usuario si desea cifrar o descifrar
tarea = input("Introduce 'C' para cifrar o 'D' para descifrar: ").strip().upper()

# Procesar el texto según la tarea
if tarea == 'C':
    resultado = cifrar_bloques(texto, tamano_bloque)
    print(f"Texto cifrado: {resultado}")
elif tarea == 'D':
    resultado = descifrar_bloques(texto, tamano_bloque)
    print(f"Texto descifrado: {resultado}")
else:
    print("Opción no válida. Introduce 'C' para cifrar o 'D' para descifrar.")

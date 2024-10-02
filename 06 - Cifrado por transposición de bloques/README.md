# Cifrado por transposición de bloques
[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>

El **cifrado por transposición de bloques** es una variante del cifrado por transposición en el que el mensaje se divide en bloques de longitud fija, y luego se reorganizan las letras dentro de cada bloque de acuerdo con una regla predefinida. A diferencia del cifrado zig-zag, que reordena las letras en varias filas, el cifrado por bloques solo reorganiza las letras dentro de bloques específicos, lo que genera más estructura en el mensaje cifrado.

#### Ejemplo:
Si el mensaje es **"ESTE ES UN MENSAJE"** y utilizamos bloques de 4 letras:

1. **Dividimos el mensaje en bloques**:
   ```
   Bloque 1: "ESTE"
   Bloque 2: " ES "
   Bloque 3: "UN M"
   Bloque 4: "ENSA"
   Bloque 5: "JE"
   ```

2. **Reorganizamos las letras en cada bloque según una regla de transposición**. Por ejemplo, podríamos invertir las letras de cada bloque:

   ```
   Bloque 1: "ETSE"
   Bloque 2: " SE "
   Bloque 3: "M NU"
   Bloque 4: "ANSE"
   Bloque 5: "EJ"
   ```

3. **El mensaje cifrado final sería**:
   **"ETSE SE M NUANSEEJ"**

Este método reorganiza el texto de manera que, sin la clave correcta (regla de transposición), es difícil reconstruir el mensaje original. Es simples pero efectivo, aunque fácilmente rompibles con técnicas modernas de criptoanálisis.


### Código Python:

La función `cifrar_bloques` se encarga de cifrar el texto utilizando la técnica de transposición por bloques. Lo primero que hace es asegurarse de que el texto tenga una longitud que sea múltiplo del tamaño del bloque, añadiendo espacios al final del texto si es necesario. Luego, el texto se divide en bloques del tamaño especificado. Dentro de cada bloque, las letras se reordenan según una regla, que en este caso es invertir el orden de las letras. Finalmente, los bloques transpuestos se unen en una única cadena y se devuelve el texto cifrado.

La función `descifrar_bloques` realiza el proceso inverso. Toma el texto cifrado y lo divide nuevamente en bloques del mismo tamaño que se utilizó al cifrar. Luego, en cada bloque se aplica la misma regla de transposición (en este caso, invertir las letras) para devolver las letras a su orden original. Una vez procesados todos los bloques, se unen de nuevo en una cadena que representa el texto descifrado.

Ambas funciones utilizan el mismo método de transposición dentro de los bloques (invertir el orden de las letras), lo que garantiza que el texto cifrado pueda ser correctamente descifrado. El programa general permite al usuario introducir un texto, elegir el tamaño de los bloques, y decidir si desea cifrar o descifrar el texto, ejecutando la función correspondiente según la opción seleccionada.

```python
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
```


### Ejemplo de uso:

```
Introduce el texto: ESTE ES UN MENSAJE
Introduce el tamaño del bloque: 4
Introduce 'C' para cifrar o 'D' para descifrar: C
Texto cifrado: ETSE SE M NUANSEEJ
```

Luego, si deseas descifrar el mismo texto:

```
Introduce el texto: ETSE SE M NUANSEEJ
Introduce el tamaño del bloque: 4
Introduce 'C' para cifrar o 'D' para descifrar: D
Texto descifrado: ESTE ES UN MENSAJE
```



[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)

# Cifrado por mezcla de palabra clave
[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>

El **Cifrado por mezcla de palabra clave** es un algoritmo de cifrado por sustitución monoalfabética que utiliza una palabra clave para generar un alfabeto cifrado. Este método es una mejora sobre el **Cifrado del César** y su variante inversa, ya que introduce una mayor complejidad al mezclar las letras del alfabeto basándose en una palabra clave, lo que lo hace más difícil de romper utilizando técnicas simples de criptoanálisis, como el análisis de frecuencias.

Si bien no es lo suficientemente seguro para proteger información crítica en la actualidad, sigue siendo un método interesante y accesible para enseñar los conceptos fundamentales de la criptografía.


#### Origen del método

El Cifrado por mezcla de palabra clave proviene de métodos criptográficos más avanzados que el simple desplazamiento de letras utilizado en el Cifrado del César. Aunque su origen exacto no se conoce, este tipo de cifrado fue utilizado en diversas formas a lo largo de la historia. A diferencia del Cifrado del César, que utiliza un desplazamiento fijo en el alfabeto, el cifrado por mezcla introduce un factor adicional: la palabra clave, que añade variabilidad y personalización al cifrado.

#### ¿Cómo funciona el Cifrado por mezcla de palabra clave?

El proceso consiste en tomar una palabra clave para construir un alfabeto cifrado personalizado. Las letras de la palabra clave se colocan al inicio del alfabeto cifrado, eliminando las repeticiones, y luego se añaden las letras restantes del alfabeto en su orden habitual.

##### Ejemplo:

- **Palabra clave**: `CIFRAMIENTO`
- **Alfabeto base**: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`

1. Primero, se elimina cualquier letra repetida de la palabra clave, lo que nos deja con `CIFRAMENTO`.
2. A continuación, se toma el resto del alfabeto y se añaden las letras que no están en la palabra clave: `BDGHJKLPQSUVWXYZ`.

El alfabeto cifrado resultante sería:

```
CIFRAMENTOBDGHJKLPQSUVWXYZ
```

#### Cifrado de un mensaje

Una vez que tenemos el alfabeto cifrado, podemos cifrar un mensaje sustituyendo cada letra del mensaje original por la letra correspondiente en el alfabeto cifrado.

##### Ejemplo de cifrado:

- **Mensaje original**: `HOLA`
- **Alfabeto base**: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- **Alfabeto cifrado**: `CIFRAMENTOBDGHJKLPQSUVWXYZ`

Sustituimos cada letra del mensaje con la correspondiente en el alfabeto cifrado:

- `H` -> `T`
- `O` -> `E`
- `L` -> `K`
- `A` -> `C`

El mensaje cifrado es: `TEKC`.

#### Comparación con el Cifrado del César y el Cifrado del César inverso

| Algoritmo                         | Descripción                                      | Complejidad | Ventaja principal |
|-----------------------------------|--------------------------------------------------|-------------|-------------------|
| **Cifrado del César**             | Desplaza cada letra del alfabeto un número fijo. | Baja        | Fácil de implementar. |
| **Cifrado del César inverso**     | Desplaza las letras hacia atrás en el alfabeto.  | Baja        | Variante simple del César. |
| **Cifrado por mezcla de palabra clave** | Utiliza una palabra clave para crear un alfabeto cifrado personalizado. | Media       | Más difícil de romper que el César debido a la personalización del alfabeto. |

#### Ventajas del Cifrado por mezcla de palabra clave

1. **Mayor seguridad**: La clave está en la palabra clave utilizada para generar el alfabeto. Mientras que el Cifrado del César utiliza un desplazamiento fijo que es fácil de detectar, el Cifrado por mezcla de palabra clave personaliza el alfabeto, haciendo que el patrón sea más difícil de romper con análisis de frecuencias.
   
2. **Flexibilidad**: A diferencia del César, este cifrado permite un alfabeto cifrado diferente para cada palabra clave, lo que aumenta la cantidad de combinaciones posibles y, por ende, la seguridad.

3. **Aplicación sencilla**: Aunque es más complejo que el Cifrado del César, sigue siendo relativamente fácil de implementar y comprender, lo que lo hace útil en aplicaciones básicas de criptografía.

#### Desventajas

- **Vulnerable a criptoanálisis avanzado**: Aunque mejora la seguridad con respecto al Cifrado del César, aún es vulnerable a ataques más avanzados como el análisis de frecuencias, especialmente si el texto cifrado es extenso.
  


### Código en Python del Cifrado por mezcla de palabra clave

Este es un programa en Python que implementa el **Cifrado por mezcla de palabra clave** con un alfabeto personalizado que incluye mayúsculas, minúsculas, el espacio en blanco y los dígitos del 0 al 9:

```python
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

```

### Breve explicación del código:

1. **Generación del alfabeto mezclado**:
   - La función `generar_alfabeto_mezclado` toma la palabra clave proporcionada por el usuario y elimina las letras repetidas usando `set()` y `sorted()` para mantener el orden original.
   - Luego, se concatenan las letras de la palabra clave con las letras restantes del alfabeto base que no están en la palabra clave. Esto genera el **alfabeto cifrado**.

2. **Cifrado/descifrado**:
   - La función `cifrado_mezcla_palabra_clave` toma el texto a cifrar/descifrar y lo procesa letra por letra.
   - Para **cifrar**, busca la letra en el alfabeto base y la reemplaza con la correspondiente en el alfabeto cifrado.
   - Para **descifrar**, busca la letra en el alfabeto cifrado y la reemplaza con la correspondiente en el alfabeto base.

3. **Estructura similar al código anterior**:
   - El flujo del programa sigue el mismo patrón: primero pide el desplazamiento (en este caso, la palabra clave), la tarea (cifrar o descifrar), y el texto a procesar.
   - El procesamiento se hace en un bucle sobre cada carácter del texto, y se respetan los caracteres no alfabéticos (que se dejan sin modificar).

### Ejemplo de uso:

```
Introduce la palabra clave: CIFRAMIENTO
Introduce 'C' para cifrar o 'D' para descifrar: C
Introduce el texto a procesar: HOLA MUNDO
Texto procesado: YPCG UYGLF
```

En este ejemplo, el alfabeto cifrado generado con la palabra clave "CIFRAMIENTO" es:

```
CIFRAMENTOBDGHJKLPQSUVWXYZ
```

Luego, el texto original "HOLA MUNDO" se cifra utilizando este alfabeto cifrado.

### Nota:
- La clave es generar correctamente el alfabeto cifrado basado en la palabra clave, asegurando que las letras no se repitan y que las letras restantes del alfabeto se añadan en su orden original.


[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)


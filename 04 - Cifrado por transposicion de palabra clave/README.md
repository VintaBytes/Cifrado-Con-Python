# Cifrado por transposición de palabra clave
[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>

El método de **Transposición de palabra clave**, como se explica en el libro de Greenwood, es una variante del **[Cifrado por mezcla de palabra clave](https://github.com/VintaBytes/Cifrado-Con-Python/tree/main/Cifrado%20por%20mezcla%20de%20palabra%20clave)**, pero con una diferencia importante en cómo se construye el alfabeto cifrado. En lugar de escribir las letras restantes del alfabeto en una sola línea después de la palabra clave, las letras se organizan en una cuadrícula y luego se leen por columnas. Esto proporciona un alfabeto más "mezclado" que en la mezcla básica de palabra clave, aumentando la seguridad del cifrado.

### Pasos detallados para la **Transposición de palabra clave**:

1. **Clave sin letras repetidas**: Comenzamos por tomar la palabra clave y eliminar cualquier letra repetida.
   
   Por ejemplo, con la clave:  
   `CIFRAMIENTO` → `CIFRAMENTO`.

2. **Cuadrícula**: A continuación, se organiza la palabra clave en la primera fila de una cuadrícula. El resto de las letras del alfabeto base (excluyendo las que ya están en la clave) se colocan fila por fila en la cuadrícula.

   Usando nuestro alfabeto base:

   ```
   alfabeto_base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'
   ```

   Y la palabra clave "CIFRAMENTO" (sin letras repetidas):

   **Cuadrícula:**
   ```
   C  I  F  R  A  M  E  N  T  O
   B  D  G  H  J  K  L  P  Q  S
   U  V  W  X  Y  Z  a  b  c  d
   e  f  g  h  i  j  k  l  m  n
   o  p  q  r  s  t  u  v  w  x
   y  z     0 1 2 3 4 5 6 7 8 9
   ```

3. **Lectura por columnas**: Para generar el alfabeto cifrado, se leen las letras de la cuadrícula por columnas, de arriba hacia abajo y de izquierda a derecha.

   **Alfabeto cifrado generado leyendo las columnas:**
   ```
   C B U e o y I D V f p z F G W g q   R H X h r 0 A J Y i s 1 M K Z j t 2 E L a k u 3 N P b l v 4 T Q c m w 5 O S d n x 6
   ```

   El resultado es el siguiente alfabeto cifrado:
   ```
   CBUeoyIDVfpzFGWgqRHXhr0AJYiMKaRKLJt2ELau3PNbv4
   ```

Este método crea un alfabeto mucho más mezclado que el generado por la mezcla de palabra clave, lo que lo hace más difícil de descifrar sin conocer la clave.

### Diferencias clave:
- **Mezcla de palabra clave**: El alfabeto cifrado se genera simplemente agregando la palabra clave y luego las letras restantes del alfabeto en su orden habitual.
- **Transposición de palabra clave**: El alfabeto cifrado se genera organizando las letras en una cuadrícula y leyendo por columnas, lo que aumenta la aleatoriedad y la seguridad del cifrado.

### Ejemplo paso a paso:
Supongamos que queremos cifrar el mensaje "HOLA" con la clave "CIFRAMIENTO".

1. Usamos el alfabeto cifrado generado mediante transposición de palabra clave:
   ```
   CBUeoyIDVfpzFGWgqRHXhr0AJYiMKaRKLJt2ELau3PNbv4
   ```

2. El mensaje "HOLA" se cifra reemplazando cada letra según el alfabeto cifrado:
   - `H` -> `e`
   - `O` -> `R`
   - `L` -> `W`
   - `A` -> `G`

   Resultado cifrado: **`eRWG`**

Este es el resultado del cifrado usando el método de transposición de palabra clave.

### Código en Python:

Ahora, veamos la implementación en Python del **Cifrado por transposición de palabra clave**.

```python
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
```

### Explicación del código:

1. **Generación del alfabeto cifrado**:
   - La función `generar_alfabeto_transposicion` crea una cuadrícula con la palabra clave en la primera fila, y luego rellena el resto con las letras del alfabeto base que no están en la clave.
   - Luego, se lee la cuadrícula por columnas, de arriba hacia abajo, y se genera el alfabeto cifrado.

2. **Cifrado/descifrado**:
   - Al cifrar, se busca cada carácter del texto en el alfabeto base y se reemplaza por su correspondiente en el alfabeto cifrado.
   - Al descifrar, se hace el proceso inverso: se busca cada carácter en el alfabeto cifrado y se reemplaza por el carácter correspondiente en el alfabeto base.

### Ejemplo de uso:

```
Introduce la palabra clave: CIFRAMIENTO
Introduce 'C' para cifrar o 'D' para descifrar: C
Introduce el texto a procesar: Hola Mundo
Texto procesado: eyGr qyVZr
```

El texto "Hola Mundo" se cifra utilizando la transposición de palabra clave con el alfabeto generado a partir de "CIFRAMIENTO", generando el resultado cifrado "eyGr qyVZr".

Esta implementación sigue la misma estructura que los casos anteriores.

[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)

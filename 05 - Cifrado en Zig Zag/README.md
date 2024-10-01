# Cifrado zig-zag (rail fence)
[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>


El cifrado zig-zag, también conocido como cifrado rail fence, es un tipo de cifrado por transposición en el que el mensaje se escribe en forma de zigzag en varias filas, y luego se lee fila por fila. Este método es muy visual y fácil de entender.

### Origen e historia del cifrado zig-zag:

El **cifrado zig-zag** o **cifrado rail fence** es una de las formas más simples de cifrado por transposición y tiene una historia bastante antigua. Aunque no hay un registro exacto de su origen, este tipo de cifrado ha sido utilizado desde tiempos antiguos debido a su simplicidad y efectividad para proteger mensajes de espionaje o intercepción casual.Se basa en un principio de transposición, es decir, en reordenar las letras del mensaje original de manera que sea más difícil leerlo sin conocer el método de reordenamiento. Aunque no es tan conocido o sofisticado como otros métodos criptográficos históricos, se utilizó debido a su sencillez en contextos donde la seguridad no requería métodos más complejos, pero donde era necesario evitar la lectura directa del mensaje.

#### **Uso en la Antigüedad**
- Este cifrado pudo haber sido usado en formas rudimentarias desde la antigüedad, aunque no hay evidencia directa que lo conecte con civilizaciones específicas. Su naturaleza visual lo hace fácil de entender y emplear sin tecnología avanzada.
  
#### **Edad Media y Renacimiento**
- Durante la Edad Media y el Renacimiento, los sistemas de cifrado por transposición como el zig-zag comenzaron a utilizarse en contextos militares y diplomáticos. Aunque no tenemos evidencia directa de que este cifrado en particular fuera predominante, los métodos de transposición eran comunes, ya que no alteraban las letras del mensaje, sino solo su orden.

#### **Uso militar**
- **Guerra Civil Estadounidense**: El cifrado rail fence (zig-zag) fue utilizado durante la Guerra Civil en los Estados Unidos para enviar mensajes de manera relativamente segura a través de telegramas. Dado que el cifrado rail fence solo reordena el mensaje, es fácil de cifrar y descifrar sin necesidad de herramientas complejas.
  
- **Primera y Segunda Guerra Mundial**: Aunque métodos de cifrado mucho más sofisticados se utilizaron durante las guerras mundiales, como la famosa máquina Enigma, algunos métodos de transposición más simples como el zig-zag seguían siendo útiles para comunicaciones rápidas en el campo de batalla, donde la seguridad extrema no siempre era una prioridad.

#### **Aplicaciones modernas**
Hoy en día, el cifrado rail fence es considerado un método débil y fácil de romper con las herramientas de criptoanálisis actuales. Sin embargo, se utiliza a menudo en entornos educativos para enseñar los conceptos básicos de cifrados por transposición y como un paso introductorio para aprender criptografía más avanzada.

El **cifrado zig-zag** es uno de los métodos más básicos y probablemente antiguos de cifrado por transposición, utilizado debido a su sencillez. Aunque su efectividad como método seguro es limitada, su legado en la criptografía reside en su valor educativo y en su uso en situaciones donde la seguridad no era una preocupación principal, pero sí el envío rápido y claro de mensajes reordenados.



### Ejemplo de cifrado zig-zag:

Supongamos que queremos cifrar el mensaje "ESTE ES UN MENSAJE" utilizando un cifrado zig-zag con 3 filas.

1. Escribimos el mensaje en zig-zag (rellenando por filas en el patrón):

```
E . . .   . . . U . . . E . . . J .
. S . E . E .   . N . M . N . A . E
. . T . . . S . . .   . . . S . . .
```

2. Ahora, leemos las letras por filas:
   - Fila 1: **E  UEJ**
   - Fila 2: **SEE NMAE**
   - Fila 3: **TS S**

El mensaje cifrado correctamente sería: **"E UEJSEE NMNAETS S"**.

### Implementación en Python usando nuestro alfabeto base:

Ahora que el ejemplo está claro, vamos a implementar el cifrado en Python utilizando el alfabeto base `'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'`.

### Código Python:

```python
def cifrado_zigzag(texto, num_filas):
    if num_filas == 1:
        return texto  # Si hay solo una fila, el texto no cambia

    # Inicializar las filas vacías
    filas = ['' for _ in range(num_filas)]
    
    # Usar una bandera para determinar la dirección (sube o baja por las filas)
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
```

### Explicación del código:

1. **Función `cifrado_zigzag`**:
   - Toma el texto y lo organiza en varias filas siguiendo un patrón de zig-zag.
   - Se usa una variable `bajar` que controla si estamos moviéndonos hacia abajo o hacia arriba entre las filas.
   - Se devuelve el texto cifrado combinando las filas.

2. **Función `descifrar_zigzag`**:
   - Divide el texto cifrado en las filas originales y luego reconstruye el texto original siguiendo el patrón de zig-zag.
   - El primer pase determina cuántas letras hay en cada fila, y el segundo pase reconstruye el texto utilizando ese patrón.

### Ejemplo de uso:

Si ciframos el texto **"ESTE ES UN MENSAJE"** con 3 filas, el resultado será:

```
Texto cifrado: E UEJSEE NMNAETS S
Texto descifrado: ESTE ES UN MENSAJE
```

Este código sigue la estructura de los ejemplos anteriores, utilizando nuestro alfabeto base y la misma estructura que los casos anteriores.

[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)


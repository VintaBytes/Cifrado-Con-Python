# Cifrado Inverso del César 
[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>


El **Cifrado inverso del César** es una variante del [cifrado César](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/Cesar/cifrado_cesar.py), pero en lugar de desplazar las letras hacia adelante en el alfabeto, se desplazan hacia atrás. En otras palabras, si en el cifrado de César normal se realiza un desplazamiento positivo (por ejemplo, 3 posiciones hacia la derecha), en el cifrado inverso, las letras se mueven el mismo número de posiciones pero hacia la izquierda (es decir, con un desplazamiento negativo).

### Ejemplo:
Con un desplazamiento de 3 hacia atrás (inverso al César):

- **Texto original**: `PYTHON`
- **Texto cifrado**: `MVQELK`

### Proceso:
1. Se toma cada carácter del texto.
2. Se desplaza un número determinado de posiciones hacia atrás en el alfabeto, en lugar de hacia adelante.
3. Al llegar al inicio del alfabeto, se "gira" al final. Por ejemplo, desplazando la letra "A" hacia atrás 3 posiciones se convertiría en "X".

### Fórmula:
En el cifrado César normal, la fórmula para cifrar es:
Nuevo Indice = ( Indice Actual + Desplazamiento ) % Tamaño del Alfabeto

En el cifrado inverso al César, la fórmula sería:
Nuevo Indice = ( Indice Actual - Desplazamiento ) % Tamaño del Alfabeto

Este cifrado inverso es igual de simple que el César normal, pero en lugar de mover las letras hacia adelante en el alfabeto, las mueve hacia atrás. 


### Ejemplo:
Con un desplazamiento de 3:
- Texto original: `PYTHON`
- Texto cifrado: `SBWKRQ`

El proceso de descifrado simplemente invierte el desplazamiento, devolviendo las letras a su posición original.

Este cifrado es fácil de romper con técnicas de criptoanálisis, como el análisis de frecuencias, ya que mantiene los patrones de las letras del texto original. Sin embargo, su simplicidad lo hacen ideal para comenzar a desarrollar esta serie de scripts.

### Código en Python del Cifrado del César 

Aquí tenemos el código para el **Cifrado inverso al del César**, siguiendo la misma estructura que el cifrado del César. 

```python
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
```

### Diferencias entre el **Cifrado del César** y el **Cifrado inverso al del César**:

1. **Dirección del desplazamiento**:
   - En el **Cifrado del César**, el desplazamiento es positivo, es decir, las letras se mueven hacia adelante en el alfabeto.
   - En el **Cifrado inverso al del César**, el desplazamiento es negativo, lo que significa que las letras se mueven hacia atrás en el alfabeto.

2. **Proceso para cifrar/descifrar**:
   - En el **Cifrado del César**, cuando seleccionas "Cifrar", el desplazamiento es positivo, y cuando seleccionas "Descifrar", se invierte el desplazamiento para recuperar el texto original.
   - En el **Cifrado inverso al del César**, cuando seleccionas "Cifrar", el desplazamiento es negativo (las letras se desplazan hacia atrás), pero en el caso de descifrar, no se invierte el desplazamiento, ya que el desplazamiento negativo hace lo inverso.

### Ejemplo:

```
Introduce el desplazamiento: 3
Introduce 'C' para cifrar o 'D' para descifrar: C
Introduce el texto a procesar: Hola Mundo 123
Texto procesado: Elix Jrlak 890
```

### NOTA:
En este caso, cuando ciframos, estamos desplazando las letras hacia atrás en lugar de hacia adelante. Cuando desciframos, simplemente volvemos a aplicar el mismo desplazamiento, ya que el desplazamiento negativo ya está trabajando en sentido contrario al cifrado tradicional.

[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)



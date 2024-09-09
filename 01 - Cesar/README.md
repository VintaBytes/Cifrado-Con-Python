# Cifrado del César 
[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)

<span><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></span>


El **Cifrado del César** (o **César Cipher** en inglés) es uno de los métodos de cifrado más antiguos y sencillos, atribuido a Julio César. El cifrado funciona desplazando cada letra del texto original (también llamado *texto plano*) un número fijo de posiciones en el alfabeto. Por ejemplo, si se utiliza un desplazamiento de 3, la letra "A" se convierte en "D", la "B" en "E", y así sucesivamente. Al llegar al final del alfabeto, las letras "rotan", por lo que la "X" se convierte en "A", la "Y" en "B", y la "Z" en "C".

### Ejemplo:
Con un desplazamiento de 3:
- Texto original: `PYTHON`
- Texto cifrado: `SBWKRQ`

El proceso de descifrado simplemente invierte el desplazamiento, devolviendo las letras a su posición original.

Este cifrado es fácil de romper con técnicas de criptoanálisis, como el análisis de frecuencias, ya que mantiene los patrones de las letras del texto original. Sin embargo, su simplicidad lo hacen ideal para comenzar a desarrollar esta serie de scripts.

### Código en Python del Cifrado del César 

Este es un programa en Python que implementa el **Cifrado del César** con un alfabeto personalizado que incluye mayúsculas, minúsculas, el espacio en blanco y los dígitos del 0 al 9:

```python
def cifrado_cesar(texto, desplazamiento, tarea):
    # Definir el alfabeto
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789'
    resultado = ''
    
    # Ajustar desplazamiento si es descifrado
    if tarea.upper() == 'D':
        desplazamiento = -desplazamiento
    
    # Procesar cada caracter en el texto
    for caracter in texto:
        if caracter in alfabeto:
            # Encontrar la posición actual del carácter en el alfabeto
            indice_actual = alfabeto.index(caracter)
            # Calcular la nueva posición con el desplazamiento
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
resultado = cifrado_cesar(texto, desplazamiento, tarea)

# Mostrar el resultado
print("Texto procesado:", resultado)
```

### Breve explicación del código:

1. **Alfabeto personalizado**: El alfabeto contiene letras mayúsculas, minúsculas, el espacio en blanco y los dígitos del 0 al 9.
2. **Desplazamiento**: Si la tarea es descifrar, se invierte el desplazamiento.
3. **Proceso**: Se procesa cada carácter del texto, verificando si está en el alfabeto. Si es así, se aplica el desplazamiento, y si no, el carácter se deja igual (para caracteres que no están en el alfabeto).

### Ejemplo de uso:

```
Introduce el desplazamiento: 3
Introduce 'C' para cifrar o 'D' para descifrar: C
Introduce el texto a procesar: Hola Mundo 123
Texto procesado: Krnd Pxohr 456
```


[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)



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





[Volver al índice](https://github.com/VintaBytes/Cifrado-Con-Python/blob/main/README.md)

## ¿Cuáles son los operadores en Python?

### Suma

Python usa ```+``` para indicar la suma. Usar ```+``` entre dos números los suma y proporciona el total.

```
answer = 30 + 12
print(answer)

# Output: 42
```

> Los operadores se comportan igual cuando se usan números literales ```(como 42)``` o variables.

### Resta 

De manera similar, Python utiliza ```-``` para la resta. Usar ```-``` entre dos números los resta y proporciona la diferencia.

```
difference = 30 - 12
print(difference)

# Output: 18
```

### Multiplicación

```*``` es el operador de multiplicación en Python. Proporciona el producto de dos números:

```
product = 30 * 12
print(product)

# Output: 360
```

### División

Por último, ```/``` se usa para la división. Proporciona el cociente de dos números:

```
quotient = 30 / 12
print(quotient)

# Output: 2.5
```

### Uso de la división

Si debemos convertir un número de segundos en minutos y segundos para su visualización:

```
seconds = 1042
```

El primer paso consiste en determinar el número de minutos que hay en ```1042``` segundos. Con ```60``` segundos en un minuto, puede dividir por ```60``` y obtener una respuesta de ```17.3666667```. El número que le interesa simplemente es ```17```. Se recomienda redondear hacia abajo, usando lo que se conoce como división de múltiplo inferior. Para realizar una división de este tipo en Python, debe utilizar ```//```.

```
seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)

# Output: 17
```

El paso siguiente es determinar el número de segundos. Este número es el resto de ```1042``` si divide entre ```60```. Para encontrar el resto, use el operador módulo, que en Python es ```%```. El resto de ```1042 / 60``` es ```22```, que es el valor que el operador módulo proporcionará.

```
seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# Output:
# 17
# 22
```

### Orden de las operaciones

Python respeta el orden de las operaciones en matemáticas. El orden de las operaciones determina que las expresiones se deben evaluar en este orden:

1. Paréntesis
2. Exponentes
3. Multiplicación y división
4. Suma y resta

Observe que se evalúan los paréntesis antes que cualquier otra operación. Usar paréntesis le permite asegurarse de que el código se ejecute de una manera predecible y el código resulta más fácil de leer y mantener. Como resultado, el procedimiento recomendado es usar paréntesis aunque el orden de las operaciones se evalúe de la misma manera sin ellos. En las dos líneas de código siguientes, la segunda es más comprensible porque el paréntesis indica claramente qué operación se realizará primero.

```
result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
# The answer is the same in both cases - 1084
```

## Uso de números en Python

Más allá de la aritmética básica, puede usar otras operaciones en los números. Es posible que tenga que realizar un redondeo o convertir cadenas en números.

### Conversión de cadenas en números

Python admite dos tipos principales de números: números enteros (o ```int```) y número de punto flotante (o ```float```). La diferencia clave entre ambos es la existencia de un separador decimal; los enteros son números enteros, mientras que los números de punto flotante contienen un valor decimal.

Al convertir cadenas en números, debe indicar el tipo de número que desea crear. Tiene que decidir si necesita un separador decimal. Se usa ```int``` para realizar la conversión en un número entero y ```float``` para hacerlo en un número de punto flotante.

```
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# Output:
# 215
# 215.3
```

> Si usa un valor no válido para ```int``` o ```float```, recibirá un error.

### Valores absolutos

En matemáticas, un valor absoluto es el número no negativo sin su signo. El uso de un valor absoluto puede ser útil en situaciones varias, incluido el ejemplo de búsqueda para determinar la distancia entre dos planetas. Considere los cálculos siguientes:

```
39 - 16
16 - 39
```

Observe que la diferencia entre las dos ecuaciones es que los números se invierten. Las respuestas son ```23``` y ```-23```, respectivamente. Al determinar la distancia entre dos planetas, no importa el orden en el que se escriben los números, ya que la respuesta absoluta es la misma.

Use ```abs``` para convertir el valor negativo en su valor absoluto. Si hace la misma operación mediante ```abs``` (e imprime las respuestas), verá que muestra ```23``` para ambas ecuaciones.

```
print(abs(39 - 16))
print(abs(16 - 39))

# Output
# 23
# 23
```

### Redondeo

También es útil la función integrada de Python denominada ```round```. Úsela para redondear hacia arriba al entero más cercano si el valor decimal es ```.5``` o mayor, o bien hacia abajo si es menor que ```.5```.

### Biblioteca matemática

Python tiene bibliotecas para proporcionar operaciones y cálculos más avanzados. Una de las más comunes es la biblioteca ```math```. ```math``` permite hacer el redondeo con  ```floor``` y ```ceil```, proporcionar el valor de pi y muchas otras operaciones. Veamos cómo usar esta biblioteca para redondear hacia arriba o hacia abajo.

El redondeo de números permite quitar la parte decimal de un número de punto flotante. Puede optar por redondear siempre hacia arriba al número entero más cercano si usa ```ceil```, o hacia abajo si usa ```floor```.

```
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# Output
# 13
# 12
```

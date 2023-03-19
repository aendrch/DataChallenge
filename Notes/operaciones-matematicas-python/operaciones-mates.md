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

## Estructura de instrucciones "if"

Para expresar la lógica condicional en Python, se usan instrucciones ```if```. Al escribir una instrucción ```if```, se basa en otro concepto que se describe en este módulo, el de los operadores matemáticos. Python admite los operadores lógicos comunes de matemáticas: igual, no igual, menor que, menor o igual que, mayor que y mayor o igual que. Probablemente esté acostumbrado a ver que estos operadores se muestran mediante símbolos, que también es la forma en que se representan en Python.

* Es igual que: ```a == b```
* No es igual a: ```a != b```
* Menor que: ```a < b```
* Menor o igual que: ```a <= b```
* Mayor que: ```a > b```
* Mayor o igual que: ```a >= b```

### Expresiones de prueba

Debe usar una instrucción ```if``` para ejecutar código solo si se cumple una condición concreta. Lo primero que hace al escribir una instrucción ```if``` es comprobar la condición mediante una _expresión de prueba_. Después, se determina si la instrucción se evalúa como ```True``` o ```False```. Si es ```True``` se ejecuta el siguiente bloque de código con sangría:

```
a = 97
b = 55
# test expression
if a < b:
    # statement to be run
    print(b)
```

En este ejemplo, ```a < b``` es la expresión de prueba. El programa evalúa la expresión de prueba y, después, ejecuta el código dentro de la instrucción ```if``` solo si la expresión de prueba es ```True```. Si evalúa la expresión, sabe que es ```False```, por lo que no se ejecutará ningún código que escriba en la instrucción ```if```.

> En Python, ```None``` y ```0``` también se interpretan como ```False```.

### Estructura de instrucciones ```if```

Use una instrucción ```if``` si quiere ejecutar código solo si se cumple una condición concreta. La sintaxis de una instrucción if siempre es la siguiente:

```
if test_expression:
    # statement(s) to be run
```

Por ejemplo:

```
a = 93
b = 27
if a >= b:
    print(a)
```

En Python, se debe aplicar sangría al cuerpo de una instrucción if. Siempre se ejecutará cualquier código que siga a una expresión de prueba que no tenga sangría:

```
a = 24
b = 44
if a <= 0:
    print(a)
print(b)
```

Salida: ```44```

En este ejemplo, la salida es ```44``` ya que la expresión de prueba es ```False``` y la instrucción ```print(b)``` no tiene sangría en el mismo nivel que la instrucción ```if```.

### ¿Qué son las instrucciones "else" y "elif"?

¿Qué ocurre si también quiere que el programa ejecute un fragmento de código cuando la expresión de prueba es ```False```? ¿O bien, qué ocurre si quiere incluir otra expresión de prueba? Python tiene otras palabras clave que puede usar para crear instrucciones ```if``` más complejas, ```else``` y ```elif```. Al usar ```if```, ```else``` y ```elif``` de forma conjunta, puede escribir programas complejos con varias expresiones de prueba e instrucciones para ejecutar.

### Uso de ```else```

Sabe que cuando se usa una instrucción ```if```, el cuerpo del programa solo se ejecutará si la expresión de prueba es ```True```. Para agregar más código que se ejecute cuando la expresión de prueba sea ```False```, debe agregar una instrucción ```else```.

Ahora se volverá al ejemplo de la sección anterior:

```
a = 93
b = 27
if a >= b:
    print(a)
```

En este ejemplo, si ```a``` no es mayor o igual que ```b```, no ocurre nada. Imagine que en su lugar quiere imprimir ```b``` si la expresión de prueba es ```False```:

```
a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)
```

Si la expresión de prueba es ```False```, se omite el código del cuerpo de la instrucción ```if``` y el programa continúa ejecutándose desde la instrucción ```else```. La sintaxis de una instrucción ```if/else``` siempre es la siguiente:

```
if test_expression:
    # statement(s) to be run
else:
    # statement(s) to be run
```

### Uso de ```elif```

En Python, la palabra clave ```elif``` es la abreviatura de _else if_. El uso de instrucciones ```elif``` permite agregar varias expresiones de prueba al programa. Estas instrucciones se ejecutan en el orden en que se escriben, por lo que el programa escribirá una instrucción ```elif``` solo si la primera instrucción ```if``` es ```False```. Por ejemplo:

```
a = 93
b = 27
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")
```

La instrucción ```elif``` de este bloque de código no se ejecutará, porque la instrucción ```if``` es ```True```.

La sintaxis de una instrucción ```if/elif``` siempre es la siguiente:

```
if test_expression:
    # statement(s) to be run
elif test_expression:
    # statement(s) to be run
```

### Combinación de instrucciones ```if```, ```elif``` y ```else```

Puede combinar instrucciones ```if```, ```elif``` y ```else``` para crear programas con lógica condicional compleja. Recuerde que una instrucción ```elif``` solo se ejecuta cuando la condición ```if``` es ```false```. Tenga en cuenta también que un bloque ```if``` solo puede tener un bloque ```else```, pero puede tener varios bloques ```elif```.

Ahora se volverá a examinar el ejemplo con una instrucción ```elif``` agregada:

```
a = 93
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")
```

Un bloque de código que usa los tres tipos de instrucciones tiene la sintaxis siguiente:

```
if test_expression:
    # statement(s) to be run
elif test_expression:
    # statement(s) to be run
elif test_expression:
    # statement(s) to be run
else:
    # statement(s) to be run
```

### Uso de lógica condicional anidada

Python también admite la lógica condicional anidada, lo que significa que puede anidar instrucciones ```if```, ```elif``` y ```else``` para crear programas aún más complejos. Para anidar condiciones, aplique sangría a las condiciones internas y todo lo que esté en el mismo nivel de sangría se ejecutará en el mismo bloque de código:

```
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")
```

Este fragmento de código genera la salida ```a is less than b```.

La lógica condicional anidada sigue las mismas reglas que la lógica condicional convencional dentro de cada bloque de código. Este es un ejemplo de la sintaxis:

```
if test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
elif test_expression:
    # statement(s) to be run
    if test_expression:
        # statement(s) to be run
    else: 
        # statement(s) to be run
else:
    # statement(s) to be run
```



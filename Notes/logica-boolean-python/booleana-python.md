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

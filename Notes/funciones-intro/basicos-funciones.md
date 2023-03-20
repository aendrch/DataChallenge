## Aspectos básicos de las funciones de Python
	
Las funciones son el siguiente paso después de haber aprendido los conceptos básicos de programación de Python. En su forma más sencilla, una función contiene código que siempre devuelve un valor (o valores). En algunos casos, una función también tiene entradas opcionales u obligatorias.

Al empezar a escribir código que duplica otras partes del programa, se convierte en una oportunidad perfecta para extraer el código en una función. Aunque compartir código común mediante funciones es útil, también se puede limitar el tamaño del código extrayendo partes en funciones más pequeñas (y legibles).

Los programas que evitan la duplicación y evitan funciones de gran tamaño mediante funciones más pequeñas son más legibles y fáciles de mantener. También son más fáciles de depurar cuando las cosas no funcionan correctamente.

Hay varias reglas sobre las entradas de funciones que son fundamentales para aprovechar al máximo todo lo que las funciones tienen que ofrecer.

> Aunque se usa el término _entrada_ para describir las funciones que se aceptan, estos elementos normalmente se denominan _argumentos_ o _parámetros_. Para mantener la coherencia en este módulo, a las entradas las denominaremos _argumentos_.

### Funciones sin argumentos

Para crear una función, usamos la palabra clave ```dev```, seguida de un nombre, paréntesis y, después, del cuerpo con el código de función:

```
def rocket_parts():
    print("payload, propellant, structure")
```

En este caso, rocket_parts es el nombre de la función. Ese nombre va seguido de paréntesis vacíos, que indican que no se necesitan argumentos. El último es el código, con sangría de cuatro espacios. Para usar la función, debemos llamarla por su nombre usando paréntesis:

```
>>> rocket_parts()
'payload, propellant, structure'
```

La función ```rocket_parts()``` no toma ningún argumento e imprime una instrucción sobre la gravedad. Si necesitamos usar un valor que devuelve una función, podemos asignar la salida de la función a una variable:

```
>>> output = rocket_parts()
payload, propellant, structure
>>> output is None
True
```

Puede parecer sorprendente que el valor de la variable ```output``` sea ```None```. Esto se debe a que la función ```rocket_parts()``` no ha devuelto explícitamente un valor. En Python, si una función no devuelve explícitamente un valor, devuelve _implícitamente_ ```None```. Actualizar la función para devolver la cadena en lugar de imprimirla hace que la variable ```output``` tenga un valor distinto:

```
>>> def rocket_parts():
...     return "payload, propellant, structure"
...
>>> output = rocket_parts()
>>> output
'payload, propellant, structure'
```

Si necesitamos usar el valor de la función, esta función _debe_ devolver explícitamente. De lo contrario; se devolverá _None_.

> No es necesario asignar siempre la devolución de una función. En la mayoría de los casos en los que una función no devuelve un valor (o valores) explícitamente, significa que no es necesario asignar ni usar el valor implícito _None_ que se devuelve.

### Argumentos opcionales y requeridos

En Python, varias funciones integradas requieren argumentos. Algunas funciones integradas hacen que los argumentos sean opcionales. Las funciones integradas están disponibles de inmediato, por lo que no es necesario importarlas explícitamente.

Un ejemplo de una función integrada que requiere un argumento es ```any()```. Esta función toma un objeto iterable (por ejemplo, una lista) y devuelve ```True``` si algún elemento del objeto iterable es ```True```. De lo contrario, devuelve ```False```.

```
>>> any([True, False, False])
True
>>> any([False, False, False])
False
```

Si llamamos a ```any()``` sin nigún argumento, se genera una excepción útil. El mensaje de error explica que necesitamos al menos un argumento:

```
>>> any()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: any() takes exactly one argument (0 given)
```

Podemos comprobar que algunas funciones permiten el uso de argumentos opcionales mediante otra función integrada denominada str(). Esta función crea una cadena a partir de un argumento. Si no se pasa ningún argumento, devuelve una cadena vacía:

```
>>> str()
''
>>> str(15)
'15'
```

## Uso de argumentos de función en Python

El siguiente paso es crear funciones que requieran un argumento

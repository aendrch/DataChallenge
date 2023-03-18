## Aspectos básicos de las cadenas en Python

### Inmutabilidad de las cadenas

En Python, las cadenas son inmutales. Es decir, no pueden cambiar. Esta propiedad del tipo de cadena puede ser sorprendente, ya que Python no proporciona errores al modificar cadenas.

En el ejemplo, tiene un único hecho sobre la Luna que está asignado a una variable y debe agregarle otro hecho (una oración). _Parece_ que agregar el segundo hecho podría modificar la variable, tal como este ejemplo siguiente:

```
>>> fact = "The Moon has no atmosphere."
>>> fact + "No sound can be heard on the Moon."
'The Moon has no atmosphere.No sound can be heard on the Moon.'
```

Aunque podría parecer que se ha modificado la variable ```fact```, una comprobación rápida del valor revela que el valor original no hacambiado:

```
>>> fact
'The Moon has no atmosphere.'
```

Aquí el truco es que se debe usar un valor devuelto. Al agregar cadenas, Python no modifica ninguna, sino que devuelve una cadena _nueva_ como resultado. Para mantener este resultado nuevo, asígnela a una nueva variable:

```
>>> two_facts = fact + "No sound can be heard on the Moon."
>>> two_facts
'The Moon has no atmosphere.No sound can be heard on the Moon.'
```

Las operaciones en las cadenas siempre generan cadenas nuevas como resultado.

### Acerca del uso de comillas

Puede incluir las cadenas de Python entre comillas simples, dobles o triples. Aunque se pueden usar indistintamente, es mejor utilizar un tipo de forma coherente dentro de un proyecto. Por ejemplo, en la cadena siguiente se usan comillas dobles:


```
moon_radius = "The Moon has a radius of 1,080 miles"
```

Pero cuando una cadena contiene palabras, números o caracteres especiales (una _subcadena_) que también se incluyen entre comillas, debe usar otro estilo. Por ejemplo, si en una subcadena se usan comillas dobles, incluya toda la cadena entre comillas simples, como se muestra aquí:

```
'The "near side" is the part of the Moon that faces the Earth'
```

Del mismo modo, si en alguna parte de la cadena hay comillas simples (o un apóstrofo, como en _Moon's_ en el ejemplo siguiente), incluya toda la cadena entre comillas dobles:

```
"We only see about 60% of the Moon's surface"
```

Si no se alternan las comillas simples y dobles, el intérprete de Python puede generar un error de sintaxis, como se muestra aquí:

```
>>> 'We only see about 60% of the Moon's surface'
  File "<stdin>", line 1
    'We only see about 60% of the Moon's surface'
                                       ^
SyntaxError: invalid syntax
```

Cuando el texto tiene una combinación de comillas simples y dobles, puede usar comillas triples para evitar problemas con el intérprete:

```
"""We only see about 60% of the Moon's surface, this is known as the "near side"."""
```

### Texto multilínea

Hay diferentes maneras de definir varias líneas de texto como una sola variable. Las más comunes son las siguientes:

* Usar un carácter de nueva línea (```\n```).
* Usar comillas triples (""").

Los caracteres de nueva línea separan el texto en varias líneas al imprimir la salida:

```
>>> multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
>>> print(multiline)
Facts about the Moon:
 There is no atmosphere.
 There is no sound.
```

Puede lograr el mismo resultado con las comillas triples:

```
>>> multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
>>> print(multiline)
Facts about the Moon:
 There is no atmosphere.
 There is no sound
```

## Métodos de cadena en Python

Los métodos de cadena son uno de los tipos de método más comunes en Python. A menudo tendrá que manipular cadenas para extraer información o ajustarse a un formato concreto. Python incluye varios métodos de cadena diseñados para realizar las transformaciones más comunes y útiles.

Los métodos de cadena forma parte del tipo ```str```. Esto significa que los métodos existen como variables de cadena o directamente como parte de la cadena. Por ejemplo, el método ```.title()``` se puede usar directamente con una cadena:

```
>>> "temperatures and facts about the moon".title()
'Temperatures And Facts About The Moon'
```

Y el mismo comportamiento y utilización se produce en una variable:

```
>>> heading = "temperatures and facts about the moon"
>>> heading.title()
'Temperatures And Facts About The Moon'
```

## División de una cadena

Un método de cadena común es ```.split()```. Sin argumentos, el método separará la cadena en cada espacio. Esto crearía una lista de todas las palabras o números separados por un espacio:

```
>>> temperatures = """Daylight: 260 F
... Nighttime: -280 F"""
>>> temperatures .split()
['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']
```

En este ejemplo, trabaja con varias líneas, por lo que el carácter de nueva línea (ímplicito) se puede usar para dividir la cadena al final de cada línea, y crear líneas únicas:

```
>>> temperatures .split('\n')
['Daylight: 260 F', 'Nighttime: -280 F']
```

Este tipo de división resulta útil cuando se necesita un bucle para procesar o extraer información, o bien cuando se cargan datos desde un archivo de texto.

## Búsqueda de una cadena

Algunos métodos de cadena pueden buscar contenido antes del procesamiento, sin necesidad de usar un bucle. Imagine que tiene dos oraciones que analizan las temperaturas de varios planetas y lunas, pero solo le interesan las temperaturas relacionadas con la Luna. Es decir, si las oraciones no se refieren a la Luna, no se deben procesar para extraer información.

La manera más sencilla de detectar si existe una palabra, un carácter o un grupo de caracteres determinados en una cadena es usar el operador ```in```:

```
>>> "Moon" in "This text will describe facts and challenges with space travel"
False
>>> "Moon" in "This text will describe facts about the Moon"
True
```

Un enfoque para buscar la posición de una palabra específica en una cadena consiste en usar el método ```.find()```:

```
>>> temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
>>> temperatures.find("Moon")
-1
```

El método ```.find()``` devuelve ```-1``` cuando se encuentra la palabra, o bien devuelve el índice (el número que representa la posición en la cadena). Así es como se comportaría si busca la palabra _Mars_:

```
>>> temperatures.find("Mars")
65
```

```65``` es la posición donde ```Mars``` aparece en la cadena.

Otra manera de buscar contenido consiste en usar el método ```.count()```, que devuelve el número total de repeticiones de una palabra determinada en una cadena:

```
>>> temperatures.count("Mars")
1
>>> temperatures.count("Moon")
0
```

Las cadenas en Python distinguen mayúsculas de minúsculas, lo que significa que _Luna_ y _luna_ se consideran palabras diferentes. Para realizar un a comparación sin distinguir mayúsculas de minúsculas, puede convertir una cadena en letras minúsculas mediante el método ```.lower()```:

```
>>> "The Moon And The Earth".lower()
'the moon and the earth'
```

Como sucede con el método ```.lower()```, las cadenas tienen un método ```.upper()``` que hace lo contrario y convierte todos los caracteres en mayúsculas:

```
>>> "The Moon And The Earth".upper()
'THE MOON AND THE EARTH'
```

> Al buscar y comprobar contenido, un enfoque más sólido consiste es convertir en minúsculas una cadena para que el uso de mayúsculas y minúsculas no impida una coincidencia. Por ejemplo, si va a contar el número de veces que aparece la palabra _the_, el método no contaría las veces en las que aparece _The_, aunque las dos sean la misma palabra. Puede usar el método _.lower()_ para cambiar todos los caracteres a minúsculas.

## Comprobación del contenido

Hay ocasiones en las que procesará texto para extraer información con una presentación irregular. Por ejemplo, la cadena siguiente es más fácil de procesar que un párrafo no estructurado:

```
>>> temperatures = "Mars Average Temperature: -60 C"
```

Para extraer la temperatura media en Marte, puede hacerlo con los métodos siguientes:

```
>>> parts = temperatures.split(':')
>>> parts
['Mars average temperature', ' -60 C']
>>> parts[-1]
' -60 C'
```

El código anterior confía en que todo lo que hay después de los dos puntos (```:```) es una temperatura. La cadena se divide en ```:```, lo que genera una lista de dos elementos. El uso de ```[-1]``` en las lisata devuelve el último elemento que, en este ejemplo, es la temperatura.

Si el texto es irregular, no puede usar los mismos métodos de división para obtener el valor. Debe recorrer en bucle los elementos y comprobar si los valores son de un tipo determinado. Python tiene métodos que ayudan a comprobar el tipo de cadena:

```
>>> mars_temperature = "The highest temperature on Mars is about 30 C"
>>> for item in mars_temperature.split():
...     if item.isnumeric():
...         print(item)
...
30
```

Como sucede con el método ```.isnumeric()```, ```.isdecimal()``` puede buscar cadenas que parezcan decimales.

> Le sorprenderá saber que ```"-70".isnumeric()``` devolverá ```False```. Esto se debe a que todos los caracteres de la cadena tendrían que ser numéricos y el guión (```-```) no lo es. Si tiene que comprobar números negativos en una cadena, el método ```.isnumeric()``` no funcionará.

Hay validaciones adicionales que puede aplicar en las cadenas para comprobar si hay valores. En el caso de los números negativos, el guion se agrega como prefijo al número y se puede detectar con el método ```.startswith()```:

```
>>> "-60".startswith('-')
True
```

De forma similar, el método ```.endswith()``` ayuda a comprobar el último carácter de una cadena:

```
>>> if "30 C".endswith("C"):
    print("This temperature is in Celsius")
'This temperature is in Celsius'
```

## Transformar texto

Hay otros métodos que ayudan en situaciones en las que el texto se debe transformar en algo distinto. Hasta ahora, ha visto cadenas que pueden usar _C_ para _Celsius_ y _F_ para _Fahrenheit_. Puede usar el método ```.replace()``` para buscar y reemplazar repeticiones de un carácter o grupo de caracteres:

```
>>> "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")
'Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.'
```

Como se ha mencionado antes, ```.lower()``` es una buena manera de normalizar el texto para realizar una búsqueda sin distinguir mayúsculas de minúsculas. Ahora se comprobará rápidamente si algún texto analiza las temperaturas:

```
>>> text = "Temperatures on the Moon can vary wildly."
>>> "temperatures" in text
False
>>> "temperatures" in text.lower()
True
```

Es posible que no tenga que realizar la comprobación sin distinguir mayúsculas de minúsculas todo el tiempo, pero convertir en minúsculas todas las letras es un buen enfoque cuando en el texto se usa una mezcla de mayúsculas y minúsculas.

Después de dividir el texto y realizar las transformaciones, es posible que tenga que volver a ensamblar todas las piezas. Al igual que el método ```.split()``` puede separar caracteres, el método ```.join()``` puede volver a agruparlos.

El método ```.join()``` necesita un elemento iterable (como una lista de Python) como argumento, por lo que su uso es diferente al de otros métodos de cadena:

```
>>> moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
>>> '\n'.join(moon_facts)
'The Moon is drifting away from the Earth.\nOn average, the Moon is moving about 4cm every year'
```

En este ejemplo, se usa el carácter de nueva línea ```'\n'``` para unir todos los elementos de la lista.



## Primeros programas con Python

### Un programa de Python

Para crear un programa en Python, debe almacenarlo en un archivo con extensión _.py_.

La idea de un programa es hacer algo o llevar a cabo una tarea. Para conseguir que el programa haga algo, debemos agregar las instrucciones necesarias oara que realice la tarea. Un ejemplo sería imprimir texto o calcular algo:

Ejemplo de aspecto (programa):

```
# program.py
sum = 1 + 2
print(sum)
```

### Ejecutar un programa

Para ejecutar un programa es necesario iniciarlo con Python desde una consola. Una consola es una línea de comandos que le permite interactuar con el sistema operativo. Para ejecutar un programa, debemos escribir el nombre del programa ejecutable Python, seguido del nombre del programa 

Ejemplo (Consola Linux - Ubuntu 22.04):

```
python3 program.py
```

La ejecución de este tipo de programa mostraría el siguiente resultado en la consola:

```
3
```

### Función print()

Para escribir información en la consola, puede usar la función ```print()``` e implementarla como una función principal. Como se trata de una función principal, tendrá acceso a ella si Python está instalado. Para usarlo ```print()``` en el programa, debemos asignar un argumento:

```
print("show this in the console")
```

La ejecución del programa mostraría el siguiente resultado en la consola:

```
show this in the console
```

Otro aspecto que hay que tener en cuenta es el uso de comillas dobles (""). Así es como se declara un literal de cadena, con un valor como el que se va a imprimir: "mostrar esto en la consola".

### Variables

En la codificación se trabaja con datos. Los programas funcionan con datos, por lo que es necesario tener que recordar un valor determinado durante la ejecución del programa. Para esto usamos variables.

En este ejemplo realizamos un cálculo que se almacena en variables:

```
sum = 1 + 2 # 3
product = sum * 2
print(product)
```

### Tipos de datos

Una variable asume un tipo de datos. En el programa anterior, ```sum``` obtiene el tipo ```int```. Sin embargo, hay muchos más tipos de datos. Como por ejemplo:

|Tipo		|Descripción				|Ejemplo					|
|:-----		|-----					|-----						|
|Tipo numérico	|Número, con o sin decimales		|```int, float, complex, no = 3```		|
|Tipo de texto	|Cadena de caracteres			|```str = "a literal string```			|
|Tipo booleano	|Boolean				|```continue = True```				|

Ejemplo de código en donde usamos los tipos anteriores:

```
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string
```

¿Cómo saber qué tipo tiene algo?

```
distance_to_alpha_centauri = 4.367 # looks like a float
```

Como alternativa, podemos usar la función ```type()```:

```
type(distance_to_alpha_centauri) ## <class 'float'>
```

### Operadores

Los operadores permiten realizar varias operaciones en las variables y sus valores. La idea general es que hay un lado izquierdo, un lado derecho y un operador en el medio:

```
<left side> <operator> <right side>
```

Este es el aspecto que tendría un ejemplo real del código de marcador de posición anterior:

```
left_side = 10
right_side = 5
left_side / right_side # 2
```

En este ejemplo se usa una barra diagonal (```/```) para dividir el valor ```left_side``` por el valor ```right_side```.

Python usa dos tipos de operadores: _aritmético_ y _asignación_.

### Operadores aritméticos

Con los operadores _aritméticos_, se hacen cálculos como suma, resta, división y multiplicación. Este es un subconjunto de operadores aritméticos que puede usar:

|Tipo	|Descripción						|Ejemplo			|
|:-----	|-----							|-----				|
|+	|Operador de suma que agrega dos valores juntos		|```1 + 1```			|
|-	|Operador de resta que quita el valor 			|```1 - 2```			|
|/	|Operador de división					|```10 / 2```			|
|*	|Operador de multiplicación				|```2 * 2````			|

### Operadores de asignación

Puede usar operadores de _asignación_ para asignar valores a una variable a lo largo del ciclo de vida de la variable. Estos son algunos operadores de asignación que es probable que encuentre a medida que aprende a compilar programas:

|Tipo	|Descripción								|Ejemplo			|
|:-----	|-----									|-----				|
|=	|x ahora contiene 2.							|```x = 2```			|
|+=	|x incrementado en 2. Si contenía 2 antes, ahora tiene un valor de 4 	|```x += 2```			|
|-=	|x reducido en 2. Si contenía 2 antes, ahora tiene un valor de 0.	|```x -= 2```			|
|/=	|x dividido por 2. Si contenía 2 antes, ahora tiene un valor de 1.	|```x /= 2```			|
|*=	|x multiplicado por 2. Si contenía 2 antes, ahora tiene un valor de 4	|```x *= 2```			|

### Fechas

Al compilar programas, es probable que interactúe con fechas. Una fecha en un programa suele indicar tanto la fecha del calendario como la hora.

Puede usar una fecha en varias aplicaciones, como en estos ejemplos:

* **Archivo de copia de seguridad**: El uso de una fecha como parte del nombre de un archivo de copia de seguridad es una buena manera de indicar cuándo se realizó una copia de seguridad y cuándo es necesario realizarla de nuevo.
* **Condición**: Es posible que quiera llevar una lógica específica cuando haya una fecha determinada.
* **Métrica**: Las fechas se usan para comprobar el rendimiento del código para, por ejemplo, medir el tiempo necesario para ejecutar una función.

Para trabajar con una fecha, debe importar el módulo ```date```:

```
from datetime import date
```

A continuación, puede llamar a las funciones con las que quiere trabajar. Para obtener la fecha de hoy, puede llamar a la función ```today()```:

```
date.today()
```

Para mostrar la fecha en la consola, puede usar la función ```print()```. La función ```print()``` adopta muchos tipos de datos como entrada. Aquí se muestra cómo puede mostrar la fecha de hoy:

### Conversión de tipos de datos

Quiere usar una fecha con algo, normalmente una cadena. Si, por ejemplo, desea mostrar la fecha de hoy en la consola, podría experimentar algún problema:

```
print("Today's date is: " + date.today())
```

Lo que se obtiene es un error:

```
Traceback (most recent call last):
  File "/<path>/program.py", line 4, in <module>
    print("Today's date" + date.today())
TypeError: can only concatenate str (not "datetime.date") to str
```

La última fila del mensaje le indica cuál es el problema. Está intentando usar el operador ```+``` y combinar dos tipos de datos diferentes, una cadena y una fecha.

Para que este código funcione, debe convertir la fecha en una cadena. Para realizar esta conversión, use la función de utilidad ```str()```:

```
print("Today's date is: " + str(date.today()))
```

La salida sería:

```
Today's date is: <date>
```

### Recopilación de entradas

### Entrada en la línea de comandos

Al iniciar un programa mediante ```python3```, se le asigna el nombre del archivo que se va a iniciar. También puede asignarle un conjunto de argumentos: datos a los que el programa tendrá acceso al ejecutarse. Este es el aspecto que puede tener:

```
python3 backup.py 2023-01-01
```

La cadena "2023-01-01" se puede usar como instrucción para que el programa backup.py inicie una copia de seguridad a partir de esa fecha. Lo que se consigue mediante el uso de argumentos de la línea de comandos es flexibilidad. El programa puede comportarse de forma diferente en función de su entrada externa.

### Argumentos de la línea de comandos

¿Cómo se capturan estos comandos desde la perspectiva de la codificación? Mediante el módulo ```sys```, puede recuperar los argumentos de la línea de comandos y usarlos en el programa. Observe el código siguiente:

```
import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg
```

```sys.argv``` es una matriz o estructura de datos que contiene muchos elementos. La primera posición, que se indica como ```0``` en la matriz, contiene el nombre del programa. La segunda posición, ```1```, contiene el primer argumento. Supongamos que el programa _backup.py_ contiene el código de ejemplo y lo ejecuta de la siguiente manera:

```
python3 backup.py 2023-01-01
```

A continuación, el programa genera el siguiente resultado:

```
['backup.py', '2023-01-01'] 
backup.py
2023-01-01
```

### Entrada de usuario

Otra manera de pasar datos al programa es hacer que el usuario escriba los datos. Puede codificarlo para que el programa indique al usuario que escriba información. Guarde los datos especificados en el programa y, a continuación, trabaje con ellos.

Para capturar información del usuario, use la función ```input()```. Este es un ejemplo:

```
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)
```

Supongamos que el programa ```input.py``` contiene el mismo código y lo ejecuta de la siguiente manera:

```
python3 input.py
```

Al ejecutar el programa, se le invita a escribir su nombre, por ejemplo:

```
Welcome to the greeter program
Enter your name:
```

Después de escribir un valor y presionar **Enter** (Entrar), se devuelve el saludo:

```
Welcome to the greeter program
Enter your name: Picard
Greetings Picard
```

### Trabajo con números

La función ```input()``` almacena un resultado como una cadena, por lo que es posible que el código siguiente no haga lo que quiera:

```
print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number)
```

La ejecución de este programa le invita a escribir el primer número, supongamos:```3```

```
calculator program
first number: 3
```

Después de presionar Enter (Entrar), puede escribir el segundo número, supongamos:4

```
calculator program
first number: 3
second number: 4
```

Al presionar **Enter** (Entrar), haga clic en el siguiente resultado:

```
calculator program
first number: 3
second number: 4
34
```

Probablemente ha pensado en que este programa le responda con ```7``` lugar de ```34```. ¿Qué ha fallado?

La explicación es que ```first_number``` y ```second_number``` son cadenas. Para que el cálculo funcione correctamente, debe cambiar esas cadenas a números mediante la función ```int()```. Al modificar la última línea del programa para usar ```int()```, puede resolver el problema:

```
print(int(first_number) + int(second_number))
```

Volver a ejecutar el programa con los mismos valores ahora devuelve ```7``` como respuesta:

```
calculator program
first number: 3
second number: 4
7
```

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

|Left	|Center	|Right	|
|:-----	|-----	|-----	|


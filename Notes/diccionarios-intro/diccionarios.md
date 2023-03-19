## Introducción a los diccionarios de Python

Las variables de Python pueden almacenar varios tipos de datos. Anteriormente hemos aprendido que podemos almacenar cadenas y números:

```
name = 'Earth'
moons = 1
```

Aunque este método funciona para cantidades más pequeñas de datos, puede ser cada vez más complejo cuando se trabaja con datos relacionados. Imaginemos que queremos almacenar información sobre las lunas de la Tierra y la Luna.

```
earth_name = 'Earth'
earth_moons = 1

jupiter_name = 'Jupiter'
jupiter_moons = 79
```

Observemos cómo se duplican las variables con prefijos diferentes. Esta duplicación puede resultar difícil de manejar. Como con frecuencia tendrá que trabajar con conjuntos de datos relacionado, como el promedio de precipitaciones durante varios meses en distintas ciudades, almacenar estar variables como valores individuales no es una opción viable.

Alternativamente, podemos usar diccionarios de Python.

Los diccionarios de Python permiten trabajar con conjuntos de datos relacionados. Un _diccionario_ es una colección de pares clave-valor. Piense que es como un grupo de variables dentro de un contenedor, donde la clave es el nombre de la variable y el valor es el valor almacenado en su interior.

### Creación de un diccionario

Python usa llaves (```{ }```) y dos puntos (```:```) para indicar un diccionario. Podemos crear un diccionario vacío y agregar valores más adelante, o bien rellenarlo en el momento de la creación. Cada clave o valor está separado por dos puntos y el nombre de cada clave se incluye entre comillas como un literal de cadena. Como la clave es un literal de cadena, podemos usar el nombre que sea adecuado para describir el valor.

Ahora se creará un diccionario para almacenar el nombre del planeta Tierra y el número de lunas que tiene:

``` Python
planet = {
    'name': 'Earth',
    'moons': 1
}
```



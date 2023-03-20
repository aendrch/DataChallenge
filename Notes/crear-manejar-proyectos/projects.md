## Trabajar con paquetes

La mayoría de los programas que escriba se basarán en el código escrito por otros usuarios. Este código suele tener el formato de paquetes, que son módulos o bibliotecas externos que se incluyen en el proyecto. Al igual que con cualquier proyecto que requiera un conjunto de recursos, es importante tener en cuenta cómo se asegurará de que los recursos adecuados estén disponibles para el programa.

Un buen punto de partida es aprender a administrar el programa. Una opción es que pensemos en el programa como si fuera un proyecto. Python se aproxima a este enfoque mediante algo denominado entornos virtuales.

### ¿Qué es un entorno virtual?

Tenemos una máquina de desarrollo. En esta máquina, es posible que tengamos una versión de Python instalada o una versión de una biblioteca que queramos usar. ¿Qué ocurre cuando movemos el programa a una máquina que tiene instalada una versión diferente de Python o versiones diferentes de las bibliotecas de las que depende?

Una cosa que no queremos hacer es asumir que el programa funcionará y que solo podemos instalar la última versión de las bibliotecas de las que depende. Si lo hacemos, podríamos acabar destruyendo la capacidad de los demás programas para funcionar en la máquina destino. La solución es esncontrar una manera de que la aplicación funcione de forma aislada.

La solución de Python para estos problemas es un entorno virtual. Un entorno virtual es una copia independiente de todo lo necesario para ejecutar el programa. Esto incluye el intérprete de Python y todas las bibliotecas que necesita el programa. Mediante un entorno virtual, puede asegurarse de que el programa tendrá acceso a las versiones y los recursos correctos para ejecutarse correctamente.

El flujo de trabajo básico tiene este aspecto:

1. Creamos un entorno virtual que no afecte al resto de la máquina.
2. Entramos en el entorno virtual, donde debemos especificar la versión de Python y las bibliotecas que necesita.
3. Desarrollamos el programa.

### Creación de un entorno virtual

Para crear un entorno virtual, llamamos al módulo ```venv```. El módulo espera un nombre como un argumento.

Seguimos estos pasos:

1. Vamos al directorio donde deseamos almacenar el proyecto.
2. Usamos el siguiente comando para llamar al módulo ```venv```. El comando difiere ligeramente en función del sistema operativo.

```
python -m venv env
```

En este momento, se crean automáticamente algunos directorios:

```
/env
  /bin
  /include
  /lib
```

El entorno necesita el directorio env para realizar un seguimiento de detalles como qué versión de Python y qué bibliotecas está usando. No colocamos los archivos de programa en el directorio env. Se recomienda colocar los archivos en el directorio src o algo similar. La estructura del proyecto podría tener un aspecto similar al siguiente:

```
/env
/src
  program.py
```

### Activar el entorno virtual

En este momento, ya tenemos un entorno virtual, pero no hemos empezado a usarlo. Para usarlo, debemos activarlo mediante una llamada a un script ```activate``` en el directorio ```env```. Este es el aspecto que puede tener la activación en Windows, Linux y macOS:

```
# Windows
source env/Scripts/activate

# Linux, WSL or macOS
source env/bin/activate
```

La llamada a ```activate``` cambia el símbolo del sistema. Le precede ```(env)``` y tiene un aspecto similar al de este ejemplo:

```
(env) -> path/to/project
```

En este momento, estamos dentro de su entorno virtual. Todo lo que haga se ejecuta de forma aislada.

### ¿Qué es un paquete?

Una de las principales ventajas de usar bibliotecas externas es que se acelera el tiempo de desarrollo del programa. Puede capturar este tipo de biblioteca en Internet. Pero al capturar e instalar estas bibliotecas a través de un entorno virtual, se asegura de instalar estas bibliotecas solo para el entorno virtual y no globalmente para toda la máquina.

### Instalación de un paquete

Intalemos un paquete mediante ```pip```. El comando ```pip``` usa el índice de paquetes de Python, o PyPi en su forma abreviada, para saber dónde obtener los paquetes. En el sitio web de PyPi podemos ver qué paquetes están disponibles.

Para instalar un paquete, ejecutamos ```pip install```, como en este ejemplo:

```
pip install python-dateutil
```

Si ejecutamos el comando anterior, descargaremos e instalaremos ```dateutil```, un paquete para analizar el formato de archivo .yml. Una vez instalado, podemos verlo en la lista si expandemos el directorio _lib_ en _env_, de la siguiente forma:

```
/env
  /lib
    /dateutil
```

Para ver qué paquetes están ahora instalados en el entorno virtual, podemos ejecutar ```pip freeze```. Este comando genera una lista de los paquetes instalados en el terminal:

```
python-dateutil==2.8.2
six==1.16.0
```

> La razón por la que la lista anterior contiene algo más que simplemente ```pipdate``` es que ```pipdate``` se basa en otras bibliotecas que también se capturan.

Para asegurarnos de que estos paquetes solo existen en el entorno virtual, intentamos salir del entorno mediante una llamada a ```deactivate```.

```
deactivate
```

Observamos cómo cambia el símbolo del sistema del terminal. Ya no va precedido de ```(env)``` y ha cambiado a esta apariencia:

```
path/to/project
```

### Más formas de instalar un paquete

También podemos usar los siguientes comandos para instalar un paquete:

* Tener un conjunto de archivos en la máquina desde ese origne:

```
cd <to where the package is on your machine>
python3 -m pip install .
```

* Instalar desde un repositorio de GitHub que proporciona control de versiones:

```
git+https://github.com/your-repo.git
```

* Instalar desde un archivo comprimido:

```
python3 -m pip install package.tar.gz
```

### Uso de un paquete instalado

Se recomienda llamar al directorio _src_ y agregar un archivo de Python de punto de entrada denominado _app.py_. Ahora agregamos el código para llamar a ```pipdate```:

```
from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)
```

## Trabajo con los archivos del proyecto

### Creación de un archivo del proyecto

Imaginemos que deseamos colaborar en un proyecto con otros desarrolladores. Una buena manera de colaborar es, por ejemplo, usar GitHub. No deseamos comprobar todos los archivos que tenemos, sino solo el código de la aplicación y una lista de paquetes de los que depende para que el programa funcione. ¿Por qué registrar solo una lista de paquetes y no los propios paquetes? una lista ocupa mucho menos espacio que el registro de los paquetes.

> Gracias a ```pip```, lo único que necesitamos es una lista.

### Uso compartido de un proyecyo

Para compartir el proyecto para que otros usuarios puedan trabajar en él, seguimos estos pasos:

1. Llamamos a ```pip freeze > requirements.txt```. Este comando crea un archivo requirements.txt con todos los paquetes que el programa necesita.
2. Creamos un archivo .gitignore y registramos el código de la aplicación y requirements.txt.
3. Registre el código para GitHub.

### Administración de dependencias

Los paquetes se ofrecen en distintas versiones. Cada vez que se corrige un paquete por cuestión de errores o cuando se le agregan más características, su número de versión suele cambiar. En beneficio del programa, es posible que necesitemos una versión específica de un paquete. Queremos mantener actualizado el proyecto para que usemos la última versión de un paquete.

Estas son las razones principales por las que resulta conveniente actualizar los paquetes:

* Correcciones de errores. La biblioteca que use puede tener problemas. Por ejemplo, una característica no funciona según lo previsto y el autor accede a ella para corregirla. Lo más probable es que necesitemos actualizar el paquete en cuanto se haya puesto en marcha una corrección de este tipo.
* Problemas de seguridad. El paquete puede tener una vulnerabilidad de seguridad. Una vez publicada esta corrección, queremos actualizar el paquete para velar por la seguridad de su empresa y sus clientes.
* Características adicionales. Está bien que se lancen nuevas características, aunque no es una razón de peso para actualizar el paquete. Aun así, si se lanza alguna característica que desee tener, es posible que queramos actualizar por ese motivo.

_Podemos usar cualquiera de estos enfoques para asegurarnos de que los paquetes se mantienen actualizados.

### Instalación de una versión más reciente

Podemos buscar la última versión disponible de un paquete e instalarla en cuanto sea posible.

> Comprobamos que cualquier nueva versión sea compatible con otras dependencias que podamos usar.

Para instalar una versión específica, usamos ```===``` entre el nombre del paquete y el número de versión. Este es un comando de ejemplo:

```
pip install python-dateutil===1.4
```

_El comando anterior instalaría la versión 1.4, si está disponible._

Hay muchas maneras de averiguar qué versiones están disponibles. Una forma es especificar una versión que sabe que no existe. El error resultante le mostrará qué versión existe. Este es un comando de ejemplo que usa la cadena sin sentido ```randomwords```:

```
pip install python-dateutil===randomwords
```

Esta es la salida resultante, con una lista de versiones existentes:

```
ERROR: Could not find a version that satisfies the requirement python-dateutil===randomwords (from versions: 1.4, 1.4.1, 1.5, 2.1, 2.2, 2.3, 2.4.0, 2.4.1, 2.4.1.post1, 2.4.2, 2.5.0, 2.5.1, 2.5.2, 2.5.3, 2.6.0, 2.6.1, 2.7.0, 2.7.1, 2.7.2, 2.7.3, 2.7.4, 2.7.5, 2.8.0, 2.8.1, 2.8.2)
ERROR: No matching distribution found for python-dateutil===randomwords
```

Otra opción es llamar a ```pip freeze```. La salida muestra qué versiones específicas ha instalado ya, cuando solo se le asignamos el nombre del paquete como argumento:

```
pip-autoremove==0.10.0
python-dateutil==2.8.2
six==1.16.0
```

En el ejemplo anterior se muestra que está instalada la versión 2.8.2. Si deseamos cambiarla a una versión anterior (porque otro paquete existente la necesita), podemos usar un comando como el de este ejemplo: pip install python-dateutil===2.8.0.

### Actualización de un paquete

Los paquetes cambian con el tiempo. Podemos actualizar al paquete más reciente sin especificar cuál es el número de versión exacto. Usamos este comando:

```
pip install <name of package> --upgrade
```

### Aplicación de una estrategia de actualización

Los paquetes usan algo denominado _versionamiento semántico_. Eso significa que, si observamos un número como la versión "1.2.3", podemos desglosar este número:

|Principal	|Minor		|Revisión	|
|-----		|-----		|-----		|
|1		|2		|3		|

* El número situado más a la izquierda se denomina ```Major```. Si este número aumenta, significa que se han introducido muchos cambios, por lo que ya no puede suponer que los métodos tienen el mismo nombre o el mismo número de argumentos que antes.
* El número del medio se denomina ```Minor```. Si cambia, significa que se ha agregado una característica.
* El número más a la derecha se denomina ```Patch```. Si este número aumenta, lo más probable es que se haya corregido algún error.

### Limpieza de paquetes no utilizados:

A veces, es posible que nos demos cuenta de que ya no necesitamos un determinado paquete de Python y, por tanto, deseamos quitarlo. En este caso, podemos usar ```pip uninstall```

```
pip uninstall python-dateutil
```

Sin embargo, si ejecuta pip freeze, verá cómo el comando anterior quitó solo la biblioteca python-dateutil. Esto puede ser problemático, ya que el proyecto ahora puede contener muchas bibliotecas sin utilizar que ocuparán espacio. Para borrar todo de lo que dependía este paquete, podemos usar ambos comandos de la siguiente forma:

```
pip freeze > requirements.txt
pip uninstall -r requirements.txt -y
```

> Los comandos anteriores quitarían todos los paquetes instalados, escribiéndolos primero en una lista en requirements.txt y eliminando después todos los paquetes de dicha lista.

Un enfoque mejor consiste en usar el comando ```autoremove```:

```
pip install pip-autoremove
pip-autoremove python-dateutil -y
```

Ahora, si ejecutamos ```pip freeze```, veremos que solo contiene la salida siguiente:

```
pip-autoremove==0.10.0
```

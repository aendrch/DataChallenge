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


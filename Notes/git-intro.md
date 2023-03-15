## ¿Qué es el control de versiones?

Un sistema de control de versiones (VCS) es un programa o conjunto de programas que realiza un seguimiento de los cambios en una colección de archivos. Uno de los objetivos de un VCS es recuperar fácilmente versiones anteriores de archivos individuales o de todo el proyecto. Otro objetivo es permitir que varios miembros de un equipo trabajen en un proyecto, incluso en los mismos archivos, al mismo tiempo sin que eso afecte al trabajo de los demás.

Otro nombre para un VCS es un sistema de administración de configuración de software (SCM). Los dos términos suelen usarse indistintamente; de hecho, la documentación oficial de Git se encuentra en git-scm.com. Técnicamente, el control de versiones es solo uno de los procedimientos que implica el SCM. Un VCS se puede usar para otros proyectos además de los de software, incluidos libros y tutoriales en línea.

### ¿Qué podemos hacer con un VCS? 

* Ver todos los cambios realizados en el proyecto, cuándo se hicieron los cambios y quién los efectuó.
* Incluir un mensaje con cada cambio para explicar los motivos.
* Recuperar versiones anteriores del proyecto completo o de archivos individuales.
* Crear ramas, donde los cambios se pueden hacer experimentalmente. Esta característica permite que se trabaje en varios conjuntos de cambios diferentes (por ejemplo, características o correcciones de errores) al mismo tiempo, posiblemente personas distintas, sin que ello afecte a la rama principal. Más adelante se pueden combinar los cambios que se quieren mantener en la rama principal.
* Adjuntar una etiqueta a una versión, por ejemplo, para marcar una nueva versión.

Git es un sistema distribuido, lo que significa que el historial completo de un proyecto se almacena en el cliente y en el servidor. Se pueden editar archivos sin conexión de red, protegerlos localmente y sincronizarlos con el servidor cuando una conexión esté disponible

### Terminología:

* **Árbol de trabajo**: conjunto de directorios y archivos anidados que contienen el proyecto en el que se trabaja.

* **Repositorio (repo)**: directorio, situado en el nivel superior de un árbol de trabajo, donde Git mantiene todo el historial y los metadatos de un proyecto. 

* **Hash**: número generado por una función hash que representa el contenido de un archivo u otro objeto como un número de dígitos fijo. Git usa hashes de 160 bits de longitud. Una ventaja de usar códigos hash es que Git puede indicar si un archivo ha cambiado aplicando un algoritmo hash a su contenido y comparando el resultado con el hash anterior. Si se cambia la marca de fecha y hora del archivo, pero el hash del archivo no, Git sabe que el contenido del archivo no se ha modificado.

* **Objeto**: un repositorio de Git contiene cuatro tipos de objetos, cada uno identificado de forma única por un hash SHA-1. Un objeto blob contiene un archivo normal. Un objeto árbol representa un directorio, y contiene nombres, valores hash y permisos. Un objeto de confirmación representa una versión específica del árbol de trabajo. Una etiqueta es un nombre asociado a una confirmación.

* **Confirmación**: cuando se usa como verbo, confirmar significa crear un objeto de confirmación. Esta acción toma su nombre de las confirmaciones en una base de datos. Significa que se confirman los cambios realizados para que otros usuarios también puedan verlos.

* **Rama**: serie con nombre de confirmaciones vinculadas. La confirmación más reciente en una rama se denomina nivel superior. La rama predeterminada, que se crea al inicializar un repositorio, se denomina ```main```, y suele tener el nombre ```master``` en Git. El nivel superior de la rama actual se denomina ```HEAD```. Las ramas son una característica increíblemente útil de Git porque permiten a los desarrolladores trabajar de forma independiente (o conjunta) en ramas y luego combinar los cambios en la rama predeterminada.

* **Remoto**: referencia con nombre a otro repositorio de Git. Cuando se crea un repositorio, Git crea un remoto denominado origin, que es el remoto predeterminado para las operaciones de envío e incorporación de cambios.

* **Comandos, subcomandos y opciones**: las operaciones de Git se realizan mediante comandos como ```git push``` y ```git pull```. git es el comando, mientras que ```push``` o ```pull``` es el subcomando. El subcomando especifica la operación que quiere que Git realice. Los comandos suelen ir acompañados de opciones, que usan guiones ```(-)``` o guiones dobles ```(--)```. Por ejemplo, ```git reset --hard```.

### Git y Github

GitHub es una plataforma en la nube que usa Git como tecnología principal. Simplifica el proceso de colaboración en proyectos y proporciona un sitio web, más herramientas de línea de comandos y un flujo integral que los desarrolladores y usuarios pueden usar para trabajar juntos. GitHub actúa como el repositorio remoto mencionado anteriormente.

Características:

* Issues
* Debates
* Solicitudes de incorporación de cambios
* Notificaciones
* Etiquetas
* Acciones
* Horquillas
* Proyectos


## Comandos básicos de Git

### git status

```git status``` muestra el estado del árbol de trabajo (y del área de almacenamiento provisional). Permite ver los cambios que Git está siguiendo en ese momento para decidir si quiere pedir a Git que tome otra instantánea.

### git add

```git add``` es el comando que se usa para indicar a Git que empiece a realizar un seguimiento de los cambios en determinados archivos.

El término técnico es _almacenamiento provisional_ de estos cambios. Va a usar git add para almacenar provisionalmente los cambios a fin de prepararse para una confirmación.

### git commit

Después de haber almacenado provisionalmente algunos cambios para su confirmación, puede guardar el trabajo en una instantánea si invoca al comando git ```commit```.

_Confirmar_ (o "commit") es un verbo y un sustantivo. Básicamente tiene el mismo significado que cuando se confirma en un plan o se confirma un cambio en una base de datos. Como verbo, la confirmación de cambios significa que se coloca una copia (del archivo, el directorio u otra "cosa") en el repositorio como una nueva versión.

### git log

El comando ```git log``` permite ver información sobre las confirmaciones anteriores. Cada confirmación tiene un mensaje adjunto (un mensaje de confirmación), y el comando ```git log``` permite imprimir información sobre las confirmaciones más recientes, como su marca de tiempo, el autor y un mensaje de confirmación.

### git help

Use este comando para obtener información fácilmente sobre todos los comandos que conoce hasta ahora y más.



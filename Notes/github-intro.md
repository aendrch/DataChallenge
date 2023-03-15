## ¿Qué es GitHub?

Es una plataforma en la nube que usa Git como tecnología principal. Simplifica el proceso de colaborar en proyectos y proporciona un sitio web, herramientas de la línea de comandos y un flujo global que permite a los desarrolladores y usuarios trabajar juntos. GitHub actúa el "repositorio remoto".

Entre las características clave que ofrece GitHub se incluyen las siguientes:

* Issues
* Debates
* Solicitudes de incorporación de cambio
* Notificaciones
* Etiquetas
* Acciones
* Horquillas
* Proyectos

### Incidencias

Las **incidencias** son el elemento en el que se produce la mayor parte de la comunicación entre los consumidores y el equipo de desarrollo de un proyecto. Se puede crear una _incidencia_ para analizar una amplia variedad de temas, como informes de errores, solicitudes de características, aclaraciones sobre la documentación, etc. Una vez que se ha creado una incidencia, se puede asignar a propietarios, etiquetas, proyectos e hitos. Las incidencias también se pueden asociar con solicitudes de incorporación de cambios y otros elementos de GitHub para proporcionar rastreabilidad en el futuro.

### Notificaciones

Como plataforma colaborativa, GitHub ofrece **notificaciones** para prácticamente todos los eventos que se producen en un flujo de trabajo determinado. Estas notificaciones se pueden adaptar en función de las preferencias. Por ejemplo, puede suscribirse a todas las creaciones y ediciones de incidencias de un proyecto, o bien recibir notificaciones únicamente de las incidencias en las que se le mencione. También puede decidir si recibirá notificaciones por correo electrónico, por web y dispositivo móvil, o ambos.

### Ramas

Las ramas son la manera preferida de crear cambios en el flujo de GitHub. Proporcionan aislamiento para que varias personas puedan trabajar simultáneamente en el mismo código de manera controlada. Este modelo garantiza la estabilidad entre las ramas críticas, como ```main```, a la vez que da libertad a los desarrolladores para confirmar los cambios que necesiten para alcanzar sus objetivos. Una vez que el código de una rama está listo para formar parte de la rama ```main```, puede combinarse mediante una solicitud de incorporación de cambios.

### Confirmaciones

Una **confirmación** es un cambio en uno o varios archivos de una rama. Cada vez que se crea una confirmación, se le asigna un identificador único y se realiza un seguimiento de ella, junto con la hora y el colaborador. Esto proporciona un registro de auditoría claro para todas las personas que revisen el historial de un archivo o un elemento vinculado, como una incidencia o una solicitud de incorporación de cambios.

### Solicitudes de incorporación de cambios

Una **solicitud de incorporación de cambios** es un mecanismo que sirve para indicar que las confirmaciones de una rama están listas para combinarse en otra. El desarrollador que envíe la solicitud de incorporación de cambios normalmente solicitará a uno o varios revisores que comprueben el código y aprueben la combinación. Estos revisores podrán comentar los cambios, agregar otros o usar la solicitud de incorporación de cambios para realizar un análisis más exhaustivo. Una vez que los cambios se hayan aprobado (en caso de que se requiera aprobación), la rama de origen de la solicitud de incorporación de cambios (la rama de comparación) se podrá combinar con la rama base.

### Etiquetas

Las etiquetas proporcionan una manera de categorizar y organizar las **incidencias** y las **solicitudes de incorporación** de cambios en un repositorio. A medida que cree un repositorio de GitHub, se agregarán automáticamente varias etiquetas y también se pueden crear otras nuevas.

Ejemplos:

* error
* en línea
* duplicar
* help-wanted
* mejora
* question

### Acciones

Las **acciones de GitHub** proporcionan funcionalidad de flujo de trabajo y automatización de tareas en un repositorio. Las acciones se pueden usar para simplificar los procesos del ciclo de vida de desarrollo de software e implementar la integración y la implementación continuas (CI/CD).

Se componen de lo siguiente:

* **Flujos de trabajo**: procesos automatizados que se han agregado al repositorio.
* **Eventos**: actividades que desencadenan un flujo de trabajo.
* **Trabajos**: conjunto de pasos que se ejecutan en un ejecutor.
* **Pasos**: tarea que puede ejecutar uno o varios comandos (acciones).
* **Acciones**: comandos independientes que se pueden combinar en pasos. Se pueden combinar varios pasos para crear un trabajo.
* **Ejecutores**: servidor que tiene instalada la aplicación de ejecutor de Acciones de GitHub.

### Clonación y bifurcación

GitHub proporciona varias maneras de copiar un repositorio para poder trabajar en él.

* **Clonar un repositorio**: al clonar un repositorio, se realizará una copia del repositorio y de su historial en el equipo local. Si tiene acceso de escritura al repositorio, puede enviar los cambios de la máquina local al repositorio remoto (denominado origen) a medida que se completan. Para clonar un repositorio, puede usar el comando git clone o el comando gh repo clone de la CLI de GitHub.

* **Bifurcación de un repositorio**: al bifurcar un repositorio, se realiza una copia del repositorio en la cuenta de GitHub. El repositorio principal se denomina ascendente, mientras que la copia bifurcada se conoce como origen. Una vez que haya bifurcado un repositorio en la cuenta de GitHub, puede clonarlo en el equipo local. La bifurcación permite realizar cambios libremente en un proyecto sin afectar al repositorio ascendente original. Para contribuir con cambios en el repositorio ascendente, cree una solicitud de incorporación de cambios desde el repositorio bifurcado. También puede ejecutar comandos ```git``` para asegurarse de que la copia local permanezca sincronizada con el repositorio ascendente.

¿Cuándo debería clonar un repositorio en lugar de bifurcarlo? Si está trabajando con un repositorio y tiene acceso de escritura, puede clonarlo en el equipo local. Desde allí, puede realizar modificaciones e introducir los cambios directamente en el repositorio de **origen**.

### GitHub Pages

**GitHub Pages** es un motor de hospedaje que está integrado directamente en la cuenta de GitHub. Si sigue una serie de convenciones y habilita la característica, puede crear su propio sitio estático generado a partir de código HTML y Markdown extraído directamente del repositorio.



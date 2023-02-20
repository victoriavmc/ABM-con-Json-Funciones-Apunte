# TP-Integrador    
                                                  -VictoriaVMC

Aplicacion de los conocimientos.
Se utilizo Json.
Lo que realiza estos archivos es:
Alta, Consulta, Muestra, Modificación y Baja.

######################################################################################################

                                         WORD INTRODUCTORIO DONDE SE EXPLICA:

Introducción
Tema: “Sistema de Planilla de Datos Médicos”
Aplicación de contenidos desarrollados en la materia “Programación I”. Enfocado para realizar un programa llamado “Sistema de Planilla de Datos Médicos”, en el lenguaje Python, con un archivo de funciones, menú y también se utiliza un formato ligero de intercambio de datos; un archivo “.JSON”.
Planteamiento del problema
Conocer las herramientas a utilizar para la creación del programa que resuelvan los siguientes puntos:
1.	Alta: Permite registrar nuevos datos de un médico en el listado general, proporcionando información como nombre/s, apellido/s, sexo, DNI, hospital donde realiza la residencia y su especialidad.
2.    Consulta: En el programa se implementaron 4 tipos consultas, todas ellas con el objetivo de la búsqueda de información en la base de datos previamente registrada.
3.    Modificación: Permite al usuario realizar modificaciones de los datos que se encuentran almacenados en el listado general, además de eliminar datos viejos y/o incorrectos.
4.	Baja: Con esta opción se puede eliminar los datos del sistema de un médico en específico.
Identificar los comandos apropiados de Python.  Lograr utilizar una sintaxis donde sea comprensible, legible. Se presenta el código de una manera eficiente y eficaz, donde hay funciones que simplifican el código.
En el presente trabajo académico, se explicarán los detalles de la realización del programa, su funcionamiento y objetivos.
 
Objetivos
Objetivo General:
Desarrollar un programa para poder automatizar el proceso de carga y búsqueda de datos de médicos utilizando una base de datos .JSON y el código en lenguaje Python
Objetivos Específicos:
Aplicar los conocimientos aprendidos en clases para desarrollar el código
Diseñar, construir y administrar una base de datos. Analizar la información obtenida y guardada en el .JSON. 
Clasificación de los datos según un tipo específico que se encuentran el .JSON
Lograr una buena escalabilidad en el programa realizado.
Diseñar funciones especiales con el objetivo de optimizar el código.
Organizar la realización de pruebas que verifiquen el correcto funcionamiento del programa y el alcance de este con respecto a los requisitos solicitados.

Desarrollo del tema

Herramientas y tecnologías utilizadas.

Para codificar se utilizó el editor de código Visual Studio Code. El lenguaje empleado fue Python y el formato JSON.

Para el desarrollo del trabajo, se realizó primero una selección de una problemática para poder implementar lo requerido por la materia para el trabajo.
Desarrollando un “Sistema de Planilla de Datos Médicos” 

El programa con el fin de poder administrar datos de los médicos que se encuentran realizando su residencia en distintos hospitales de la provincia, cada uno con distintas especialidades.

El programa cuenta con varias funciones para utilizar los datos de los MÉDICOS.

Una vez definida la problemática se empezó a listar los requerimientos del programa, además de armar una estructura básica para organizar la modalidad de funcionamiento, para ello, se crearon 4 archivos en Visual Studio Code.

El primer archivo, nombrado “PlanilladeMedicos”, tiene un formato JSON, ya que en él se almacenarán los datos de cada médico que se ingrese al programa en un diccionario y, a su vez, cada diccionario estará dentro de una lista global llamada “listaMedicos”.

El segundo archivo en crearse fue “Menu”, que bien como en su nombre lo explica, en este se detalló las opciones que ofrecerá el programa colocadas en un orden específico que van acorde a la forma de organización que estarían las funciones.

Los últimos dos archivos restantes, “Funciones” y “Principal”, fueron trabajados al mismo tiempo ya que en “Funciones” se encuentra el código de cada función y, en “Principal” se encuentra la estructura del programa donde se encuentran importados los 2 archivos anteriormente mencionados y un if dentro de un while que permite la interacción del usuario con el menú para elegir una opción en base a su necesidad y redirige órdenes hacia las funciones correspondientes para ejecutarlas.
Como fue mencionado anteriormente, las funciones fueron realizadas en orden acorde al menú y, cabe destacar que cada una fue ejecutada y verificada con respecto a su funcionamiento a medida que el programa se iba desarrollando.

Las primeras funciones “ArchivosJson ()” y “cargarDatos”, fueron realizadas con el objetivo de leer los datos que hay en el archivo con formato JSON y cargar datos a este, respectivamente.

La función “NuevosDatos()” corresponde a la primera opción del menú, esta permite al usuario ingresar nombre/s, apellido/s, DNI, sexo, hospital y especialidad, una vez obtenidos dichos datos, mediante una función específica para cada dato, estos se almacenan dentro de un diccionario propio del médico en particular para luego ser agregado a la lista global que está en el archivo JSON invocando a la función “CargarDatos()”.

Para la consulta de medico según su DNI se realizó la función “consultarMedicoDNI(pdni)”, la cual llama a la función “solicitudDNI()” para que el usuario ingrese el DNI del médico que desea tener información y, a su vez, se verifica que los 8 dígitos que posee un DNI. Además, al tiempo de devolver los datos requeridos por el usuario se utiliza una función “sexotipoDNI(pdni)” para dar más formalidad que trata de utilizar el mismo DNI ingresado para, primeramente, corroborar que dicho dato existe dentro de la lista global, con la función “existeDatos(pvariable)”, y para determinar que sexo tiene, y así poder designarle el titulo correcto ya sea “la médica” o “el medico”.

Las opciones 3 y 4, “Listado de médicos según el hospital” y “Listado de médicos según su especialidad” respectivamente, tienen códigos similares que en primer lugar pide al usuario ingresar el nombre del hospital o el tipo de especialidad, dependiendo del tipo de búsqueda y mediante una función de solicitud,  y que luego dicho dato se lo devuelve a la función principal, ya sea “consultarMedicoHospital(lugar)” o “consultarMedicoEspecialidad(pespecialidad)” ambos utilizando de parámetro al dato que fue ingresado que, posteriormente, se utiliza en 2 funciones internas para verificar que existe dicho dato en la lista global y para determinar el o los géneros de los médicos resultantes de la búsqueda y, a su vez, son guardados en otra lista llamada “listaGeneros” para poder devolver al usuario un resultado mejor organizado y fácilmente legible.

En el caso de la modificación de datos se realizó una función llamada “ModificarDatosDelMedico()” que posee un bucle while en donde se muestra un menú interno junto con las funciones y solicita la interacción del usuario para que elija los datos desea modificar hasta que seleccione la opción de finalizar. Cabe destacar que al modificar el primer dato pide que se ingrese el DNI del médico por única vez, es decir, si desea seguir modificando otros datos ya no será necesario que ingrese nuevamente el DNI ya que el programa ya ubicó el diccionario que utiliza dicho médico. Además, para la modificación de cada dato llama a otra función especifica de este, por ejemplo, cuando se quiere modificar el o los nombre/s de un médico, primero pide ingresar su DNI para encontrar el diccionario con la información de este, luego llama a la función “nombreMod(sgDNI)” y una vez el usuario haya ingresado el nombre modificado, este se guardará correctamente en el diccionario dentro de la lista global de médicos.

Con respecto a la eliminación de datos, esta llama a la función “seguro()” que pide al usuario ingresar el DNI del médico que desea sacar de la lista global que verifica que existe dicho dato y muestra la información contenida dentro del diccionario del médico al usuario para posteriormente preguntar si está seguro de continuar con las acción, en caso de ser positiva la respuesta ingresada se retorna a la función principal “eliminarDatos()” para nuevamente realizar la búsqueda en la lista global y utilizar el método “remove” para eliminar todos los datos del médico.

Para finalizar, la función “mostrarTodoslosMedicos()” que corresponde a la opción 6, esta posee un for para recorrer cada uno de los diccionarios de cada médico en la lista global para poder devolver todos esos datos al usuario que lo requiera.


###############################################################################################
                                                   

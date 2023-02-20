import json, string
listaMedicos = []
listagenero = [] 

def ArchivosJson():
    global listaMedicos
    try:
        with open("PlanilladeMedicos.json") as archivoJson:
            listaMedicos = json.load(archivoJson)
    except:
        print("Error al abrir el archivo")

ArchivosJson()

def cargarDatos():
    with open("PlanilladeMedicos.json", "w") as archivoJson:
        json.dump(listaMedicos, archivoJson)

#1

def solicitudNombre():
    nom = input("Ingrese su/s Nombre/s: ")
    nom = (string.capwords(nom))
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    return nom
    
def solicitudApellido():
    apellido = input("Ingrese su/s Apellido/s: ")
    apellido = apellido.upper()
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    return apellido

def solicitudGenero():
    retoma = True
    while retoma:
        genero = int(input("Cual es su género? \n 1.Femenino \n 2.Masculino \n Ingrese una opción: "))
        if genero == 1:
            genero ="Femenino"
            break
        elif genero == 2:
            genero ="Masculino"
            break
        else:
            print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
            print("Error al ingresar la opción.\n Intente Nuevamente.")
            print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    return genero
    
def solicitudDNI():
    while True:
        dni = int(input("Ingrese el DNI (Sin los puntos): "))
        contador = 0
        for indice in str(dni):
            contador +=1
        if contador == 8:
            break
        else:
            print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
            print(" Error con el DNI.\n Intente Nuevamente, pero esta vez debe tener 8 digitos!")
            print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    return dni

def solicitudHospital():
    hospital= input("Ingrese en que Hospital se encuentra haciendo la Residencia: ")
    hospital = (string.capwords(hospital))
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    return hospital

def solicitudEspecialidad():
    especialidad= input("Ingrese en que se Especializó: ")
    especialidad = (string.capwords(especialidad))
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    return especialidad
    
def NuevosDatos():
    datosAgregar= dict()

    nombre=solicitudNombre()
    apellidoS = solicitudApellido()
    tipoSexo = solicitudGenero()
    dni = solicitudDNI()
    hospital = solicitudHospital()
    especialidad= solicitudEspecialidad()

    datosAgregar["Nombre/s"] = nombre
    datosAgregar["Apellido/s"] = apellidoS
    datosAgregar["Sexo"] = tipoSexo
    datosAgregar["DNI"] = dni
    datosAgregar["Hospital"] = hospital
    datosAgregar["Especialidad"] = especialidad

    listaMedicos.append(datosAgregar)
    cargarDatos()
    print("Datos Ingresados con Exito!")

# 2 , 3 4
def peticionProcesoDNI ():
    dniIngresado = solicitudDNI()
    consultarMedicoDNI(dniIngresado)
    return dniIngresado

def existeDatos(pvariable):
    existe= False
    for listadeunsolomedico in listaMedicos:
        if pvariable == listadeunsolomedico["DNI"] or pvariable == listadeunsolomedico["Hospital"] or pvariable == listadeunsolomedico["Especialidad"]:
            existe= True
    return existe

def sexotipoDNI(pdni):
    if existeDatos(pdni):
        for listadeunsolomedico in listaMedicos:
            if pdni == listadeunsolomedico["DNI"]:
                if listadeunsolomedico["Sexo"] == 'Femenino':
                    sexoMed = "la medica"
                else:
                    sexoMed = "él medico"                      
        return sexoMed
    else:
        print("Error, el DNI ingresado no existe en la base de datos de medicos.")
  
def consultarMedicoDNI(pdni):
    genero = sexotipoDNI(pdni)
    for listadeunsolomedico in listaMedicos:
        if listadeunsolomedico["DNI"] == pdni:
            print(f" El DNI ingresado pertence a {genero}: {listadeunsolomedico['Nombre/s']}, {listadeunsolomedico['Apellido/s']} \n Se encuentra en el Hospital:{listadeunsolomedico['Hospital']}  \n Espacialista en: {listadeunsolomedico['Especialidad']} ")

def variosMedicosGeneros(PVARIABLE):
    listaGeneros = []
    if existeDatos(PVARIABLE):
        for listadeunsolomedico in listaMedicos:
            if listadeunsolomedico["Sexo"] == 'Femenino':
                listaGeneros.append("la medica")
            elif listadeunsolomedico["Sexo"] == 'Masculino':
                listaGeneros.append("él medico")  
        return listaGeneros         
    else:
        print("Error, el dato ingresado no existe en la base de datos de medicos.")

def consultarMedicoHospital(lugar):
    listagenero = variosMedicosGeneros(lugar)
    contador = 0
    muestra = 0
    if existeDatos(lugar):
        for listadeunsolomedico in listaMedicos:
            if listadeunsolomedico["Hospital"] == lugar:
                if contador == 0:
                    print(f"Segun el hospital ingresado: {lugar} . \n Se encuentran:")    
                print(f"A {listagenero[contador]}: {listadeunsolomedico['Nombre/s']}, {listadeunsolomedico['Apellido/s']} \n Espacialista en: {listadeunsolomedico['Especialidad']} \n")
                muestra += 1
            else:
                muestra +=  0
            contador += 1
        if muestra == 0 :
                print("Error, el Hospital ingresado no existe en la base de datos de medicos.")

def consultarMedicoEspecialidad(pespecialidad):
    listagenero = variosMedicosGeneros(pespecialidad)
    contador = 0
    muestra = 0
    if existeDatos(pespecialidad):
        for listadeunsolomedico in listaMedicos:
            if listadeunsolomedico["Especialidad"] == pespecialidad:
                if contador == 0:
                    print(f"Segun la especialidad ingresada: {pespecialidad} . \n Se encuentran:")    
                print(f"A {listagenero[contador]}: {listadeunsolomedico['Nombre/s']}, {listadeunsolomedico['Apellido/s']} \n En el Hospital: {listadeunsolomedico['Hospital']} \n")
                muestra += 1
            else:
                muestra +=  0
            contador += 1
        if muestra == 0 :
            print("Error, la especialidad ingresada no existe en la base de datos de medicos.")

# 5 y 7
def seguro(pvalor):
    if existeDatos(pvalor):
        while True:
            print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
            seleccion = input("Esta seguro de querer realizar acciones? -Si -No ")
            print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
            seleccion = seleccion.capitalize()
            if seleccion == "Si":
                seleccion = "Si"
                break
            elif seleccion == "No":
                seleccion = "No"
                break
            else:
                print("Error al ingresar la opción.\n Intente Nuevamente.")
    else:
        print("Debe ingresar un DNI que este en la base de datos para poder modificar.")
        print()
        seleccion = "No existe"
    return seleccion

def mostrarMenuModificacion(pcontador):
    print(""" Que dato desea modificar? (Al finalizar se volverá a consultar)""")
    if 0 == pcontador:
        print("""
            * ACLARACION:
                    PRIMERO DEBERA INGRESAR UNA SOLA VEZ
                        EL DNI DEL MEDICO AL QUE QUIERE MODIFICAR CUALQUIERA DE LOS DATOS.
                                    SOLO MODIFICARA LOS DATOS INGRESADOS DE ESE MEDICO.""")
    print("""
1. Nombre/s
2. Apellido/s
3. Género 
4. DNI
5. Hospital
6. Especialidad
0. Finalizar. """)
    modificara = int(input("\n Seleccione una opción:"))
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    return modificara

def nombreMod(sgDNI):
    if existeDatos(sgDNI):
        for unMedico in listaMedicos:
            if sgDNI == unMedico["DNI"]:
                nombre = solicitudNombre()
                unMedico["Nombre/s"] = nombre
                                
def apellidoMod(sgDNI):
    if existeDatos(sgDNI):
        for unMedico in listaMedicos:
            if sgDNI == unMedico["DNI"]:
                apellidoMod = solicitudApellido()
                unMedico["Apellido/s"] = apellidoMod

def generoMod(sgDNI):
    if existeDatos(sgDNI):
        for unMedico in listaMedicos:
            if sgDNI == unMedico["DNI"]:
                generoMod = solicitudGenero()
                unMedico["Sexo"] = generoMod

def dniMod(sgDNI):
    if existeDatos(sgDNI):
        for unMedico in listaMedicos:
            if sgDNI == unMedico["DNI"]:
                dniMod = solicitudDNI()
                unMedico["DNI"] = dniMod
                
def hospitalMod(sgDNI):
    if existeDatos(sgDNI):
        for unMedico in listaMedicos:
            if sgDNI == unMedico["DNI"]:
                hospitalMod = solicitudHospital()
                unMedico["Hospital"] = hospitalMod
                
def especialidadMod(sgDNI):
    if existeDatos(sgDNI):
        for unMedico in listaMedicos:
            if sgDNI == unMedico["DNI"]:
                especialidadMod = solicitudEspecialidad()
                unMedico["Especialidad"] = especialidadMod
                
def ModificarDatosDelMedico():
    contador = 0
    while True:
        modificar= mostrarMenuModificacion(contador)
        if modificar > 0 and modificar <= 6:
            if contador == 0:
                documento = peticionProcesoDNI()
                if existeDatos(documento):
                    contador =16
                else:
                    contador = 0
                print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
        if modificar >=1 and modificar <= 6:
            if existeDatos(documento):
                if modificar ==1:
                    nombreMod(documento)
                elif modificar ==2:
                    apellidoMod(documento)
                elif modificar ==3:
                    print("(Nuevo DNI)")
                    generoMod(documento)
                elif modificar ==4:
                    dniMod(documento)
                elif modificar ==5:
                    hospitalMod(documento)
                elif modificar ==6:
                    especialidadMod(documento)
                cargarDatos()
                print("""Los Datos han sido modificados.""")
                print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
        elif modificar == 0:
            if contador == 0:
                print("Los Datos se mantendran igual!")
                print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
            else:
                print("Los Datos se han modificado!")
                
            break
        else:
            print("""  Error al ingresar datos.\n    Intente nuevamente.""")

def eliminarDatos():
    documento = peticionProcesoDNI()
    selecciono = seguro(documento)
    if selecciono == "Si":
        for unMedico in listaMedicos:
                if documento == unMedico["DNI"]:
                    listaMedicos.remove(unMedico)
                    cargarDatos()
        print("Datos eliminado correctamente!")
    elif selecciono == "No":
        print("Los Datos se mantendran igual!")
        print()

#6
def mostrarTodoslosMedicos():
    print("Planilla de Medicos:")
    for listadeunsolomedico in listaMedicos:
        print(f"Nombre/s:{listadeunsolomedico['Nombre/s']}. Apellido/s: {listadeunsolomedico['Apellido/s']}. \n Genero: {listadeunsolomedico['Sexo']}. Dni: {listadeunsolomedico['DNI']}.    \n   Hospital: {listadeunsolomedico['Hospital']}. Especialista en: {listadeunsolomedico['Especialidad']}. \n" )
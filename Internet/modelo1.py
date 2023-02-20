import json

listadeJson = []
listaFuncion2 = list()

with open("modelo.json") as jsonfile:
    listadeJson = json.load(jsonfile)


def funcion1(plistadeJson):
    ideterminardo = int(input("Ingrese el id para averiguar su estado: "))
    for listas in plistadeJson:
        existe = ideterminardo in listas.values()
        if existe:
            nid = (listas["Id"])
            estado1 = (listas["Estado"])
    return nid, estado1


def funcion2(plistadeJson):
    lista2 = list()
    while retoma:
        edeterminado = int(
            input("Ingrese el estado para mostrar los servidores: 1- Activo 2. Inactivo "))
        if edeterminado == 1:
            edeterminado = "Activo"
            break
        elif edeterminado == 2:
            edeterminado = "Inactivo"
            break
        else:
            print("error")
    lista2.append(edeterminado)
    for listas in plistadeJson:
        existe = edeterminado in listas.values()
        if existe:
            servi = (listas["Servidor"])
            lista2.append(servi)
    return lista2


def funcion3(plistadeJson):
    contador = 0
    for listas in plistadeJson:
        existe = "Servidor" in listas.keys()
        if existe:
            contador += 1
    return contador


def funcion4(plistadeJson):
    contador = 0
    for listas in plistadeJson:
        existe = "Id" in listas.keys()
        if existe:
            contador += 1
    return contador


def funcion5(plistadeJson, df4):
    diccionarioP = dict()
    ident = (df4+1)
    diccionarioP["Id"] = ident
    concatenaServidor = (f"Servidor{ident}")
    diccionarioP["Servidor"] = concatenaServidor
    concatenaIP = (f"{ident}.{ident}.{ident}.{ident}")
    diccionarioP["IP"] = concatenaIP
    print(f"Usted Esta agregando los datos al servidor {ident}.")
    while retoma:
        estad = int(input("En que estado se encuentra? 1.Activo 2.Inactivo "))
        if estad == 1:
            estad = "Activo"
            break
        elif estad == 2:
            estad = "Inactivo"
            break
        else:
            print("error")
    diccionarioP["Estado"] = estad
    plistadeJson.append(diccionarioP)
    return (plistadeJson)


retoma = True
while retoma:
    print("1. Una función que retorne el estado de un servidor determinado por su ID.")
    print("2. Una función que retorne los servidores según un estado determinado.")
    print("3. Una función que retorne cuantos servidores hay.")
    print("4. Una función que retorne el ID máximo de las cuentas más uno.")
    print("5. Agregar nuevos datos al json.")
    selector = int(input("Que funcion desea ver? Presione 0 para salir."))
    if selector == 1:
        ide, est = funcion1(listadeJson)
        print(f"ID: {ide}. Estado: {est}")
    elif selector == 2:
        listaFuncion2 = funcion2(listadeJson)
        print(listaFuncion2)
    elif selector == 3:
        cantidad = funcion3(listadeJson)
        print(f"Hay {cantidad} de servidores.")
    elif selector == 4:
        ide = funcion4(listadeJson)
        print(f"El ID máximo de las cuentas es: {ide} y más uno es: {ide+1}. ")
    elif selector == 5:
        ide = funcion4(listadeJson)
        listadeJson = funcion5(listadeJson, ide)
        with open("modelo.json", "w") as jsonfile:
            json.dump(listadeJson, jsonfile)
        print("Cargado con exito!")
        print(listadeJson)
    elif selector == 0:
        break
    else:
        print("error")

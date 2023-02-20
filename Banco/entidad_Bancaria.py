from plantillaSepara_VictoriaVMC import *
import json
ListaJsonBancaria = []

# Abrir y Cargar el json
with open("Entidad_Bancaria.json") as jsonfile:
    ListaJsonBancaria = json.load(jsonfile)

contadoNnumerico = 0


def funcionPeticion():
    retoma = True
    while retoma:
        contador = 0
        cuit = int(input("Ingrese su CUIT: "))
        for indice in str(cuit):
            contador += 1
        if contador == 11:
            break
        else:
            print(
                "\n Error con su CUIT.\n Ingrese Nuevamente, pero esta vez debe tener 11 digitos!")
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    saldo = float(input("Ingrese su Saldo: "))
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    while retoma:
        saldoT = input("Ingrese saldo negativo. S o N:")
        saldoT = saldoT.capitalize()
        if saldoT == "S":
            print("\n Puede retirar dinero si no tiene saldo suficiente.")
            break
        elif saldoT == "N":
            print("\n NO puede retirar dinero si no tiene saldo suficiente")
            break
        else:
            a_errorIntenteNuevamente()
    return cuit, saldo, saldoT


def funcion1(pListadoJson):
    for lista in (pListadoJson):
        print(lista)


def funcion2(pListadoJson):
    todaLaCuenta = list()
    ncuenta = int(input("Ingrese el número de cuenta: \n"))
    for listados in pListadoJson:
        existe = ncuenta in listados.values()
        if existe:
            todaLaCuenta.append(listados)
    return todaLaCuenta


def funcion3(plistadoJson):
    mostrar = ""
    ncuenta = int(input("Ingrese el número de cuenta: "))
    for listados in plistadoJson:
        existe = ncuenta in listados.values()
        if existe:
            if (listados["Saldo Negativo:"]) == "N":
                mostrar = ("Presenta Saldo: Negativo")
            elif (listados["Saldo Negativo:"]) == "S":
                mostrar = ("Presenta Saldo: Positivo")
    return mostrar


def funcion4(plistadoJson):
    contador = 0
    contador2 = 0
    for listados in plistadoJson:
        if (listados["Saldo Negativo:"]) == "N":
            contador += 1
        elif (listados["Saldo Negativo:"]) == "S":
            contador2 += 1
    return contador, contador2


retome = True
while retome:
    listadosaber = list()
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    print("""1- Función que muestre un Listado de todas las cuentas.
2- Función que retorne una cuenta según un número de cuenta
3- Función que retorne si la cuenta tiene saldo negativo
4- Función que retorne la cantidad de cuentas según valor de parámetro
    Si es “S” todas las cuentas que pueden tener saldo negativo
    Si es “N” todas las cuentas que NO pueden tener saldo negativo
5- Función que pida al usuario los datos necesarios para generar una nueva Cuenta
Codifique una interacción con el usuario que utilice las funciones previamente desarrolladas.
0- SALIR
""")
    selecciona = int(input("Seleccione una opcion: "))
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    if selecciona == 1:
        funcion1(ListaJsonBancaria)
    elif selecciona == 2:
        listadosaber = (funcion2(ListaJsonBancaria))
        if len(listadosaber) == 0:
            print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
            print("No existe una cuenta con ese número.")
        else:
            print(listadosaber)
    elif selecciona == 3:
        muestro = (funcion3(ListaJsonBancaria))
        if muestro == "":
            print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
            print("No existe una cuenta con ese número.")
        else:
            print(muestro)
    elif selecciona == 4:
        N, S = funcion4(ListaJsonBancaria)
        print(f"Presenta {N} cantidad de cuentas con saldo N")
        print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
        print(f"Presenta {S} cantidad de cuentas con saldo S")
    elif selecciona == 5:
        quedeLindo = dict()
        contadornumerico += 1
        cuit, monto, saldoNegativo = funcionPeticion()
        quedeLindo["Número:"] = contadornumerico
        quedeLindo["CUIT:"] = cuit
        quedeLindo["Saldo:"] = monto
        quedeLindo["Saldo Negativo:"] = saldoNegativo
        ListaJsonBancaria.append(quedeLindo)
        with open("Entidad_Bancaria.json", "w") as jsonfile:
            json.dump(ListaJsonBancaria, jsonfile)
        a_separador()
    elif selecciona == 0:
        a_chau()
        break
    else:
        a_errorIntenteNuevamente()

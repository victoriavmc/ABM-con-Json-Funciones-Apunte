from plantillaSepara_VictoriaVMC import *
punto8 = {}
def menu():
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")

repeti = True
while repeti:
    a_separadorMismoEjercicio()
    menu()
    a_separadorMismoEjercicio()
    selecciona= int (input ("Que realizara?: "))
    print("")
    if selecciona == 1:
        nombre = input("Ingrese el Nombre: ")
        nombre= nombre.capitalize()
        existe = nombre in punto8
        if existe == True:
            for clave, valor in punto8.items():
                if clave == nombre:
                    print(f"El número de {clave} es: {valor}")                 
                    selec = int(input("Desea modificarlo? 1. Si 2. No "))
                    a_separadorMismoEjercicio()
                    if selec ==1:
                        telefono = int(input("Ingrese el Telefono: "))
                    elif selec ==2:
                        print("")
                    else:
                        print("")
        else:
            telefono = int(input("Ingrese el Telefono: "))
        #Agregar un diccionario, la clave sera nombre y el telefono es valor.
        punto8[nombre] = [telefono]
    elif selecciona ==2:
        letra = input("Ingrese la letra: ")
        letra= letra.capitalize()
        a_separadorMismoEjercicio()
        for clave, valor in punto8.items():
            for letrano in clave[0]:
                if(letrano == letra):
                    print(f"El número de {clave} es: {valor}")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    elif selecciona==3:
        nombre = input("Ingrese nombre de quien va a borrar: ")
        nombre= nombre.capitalize()
        a_separadorMismoEjercicio()
        existe = nombre in punto8
        if existe == True :
            seguro = int(input("Seguro quiere borrar? 1. Si 2. No"))
            a_separadorMismoEjercicio()
            if seguro == 1:
                del punto8[nombre]          
                print("Se ha eliminado con exito! ")
                print(punto8)
            elif seguro ==2:
                print(f"Seguira de contacto {nombre} ")
            else:
                print("Error 404") #No puse un while para volver a preguntar entonces que salga de la agenda de manera automatica lola.
                exit()
        else:
            print("El contacto no existe.")
    elif selecciona==4:
        #leer uno a uno
        for clave, valor in punto8.items():
            print(f"El número de {clave} es: {valor} ")
    elif selecciona == 0:
        repeti =False
    else:
        a_errorIntenteNuevamente()

def menu():
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    print("""    1- Agregar un medico a la base de datos.
    2- Consultar medico según su DNI.
    3- Listado de medicos según el hospital.
    4- Listado de medicos según su especialidad.
    5- Modificar datos de un médico según DNI.
    6- Mostras planilla de todos los medicos. 
    7- Dar debaja a la residencia según DNI.
    0- Para salir. """)
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    seleccion = int(input("Ingrese una opción:"))
    print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
    return seleccion


def chau():
    print("""- Profesor:
    
- Estudiantes:
               VictoriaVMC\n

-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-\n
               MUCHAS GRACIAS!\n
-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-""")

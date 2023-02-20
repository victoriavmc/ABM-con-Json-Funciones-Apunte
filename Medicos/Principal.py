from Funciones import *
from Menu import *

while True:
    opcion= menu()
    if opcion == 1:
        NuevosDatos()
    elif opcion == 2:
        peticionProcesoDNI()
    elif opcion == 3:
        hospi = solicitudHospital()
        consultarMedicoHospital(hospi)
    elif opcion == 4:
        esp = solicitudEspecialidad()
        consultarMedicoEspecialidad(esp)
    elif opcion == 5:
        ModificarDatosDelMedico()
    elif opcion == 6:
        mostrarTodoslosMedicos()
    elif opcion == 7:
        eliminarDatos()
    elif opcion == 0:
        chau()
        break
    else:
        print("""  Error al ingresar datos.\n    Intente nuevamente.""")
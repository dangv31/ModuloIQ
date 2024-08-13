from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Observacion import Observacion
from src.ui_main.Cambiar_Estado import Cambiar_Estado


class Editar_Sede:
    @classmethod
    def editar_sede(cls, cuenta):
        nombre_sede = input("Ingrese el nombre de la sede: ")
        sede_l = Gestor_Base.buscar_objeto(nombre_sede, "Sede")
        while True:
            if sede_l == None:
                print("Esa sede no existe")
                from src.ui_main.Menu_inicial import Menu_inicial
                return Menu_inicial.menu_inicial_Administrativo(cuenta)
            else:
                break
        id = sede_l[0]
        sede = sede_l[1]
        sede.imprimir_info()
        print("1. Actualizar datos basicos")
        if sede.estado:
            print("2. Deshabilitar sede")
        else:
            print("2. Habilitar sede")
        print("3. Volver al menu inicial")
        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
                if 1 <= opcion <= 3:
                    break
                else:
                    print("Ingrese un numero dentro del rango")
            except ValueError:
                print("Ingrese un numero")
        if opcion == 1:
            while True:
                sede.imprimir_info()
                while True:
                    opcion_actualizar = input("Ingrese el nombre del campo que quiere modificar (Personal, Pacientes y Estado no son modificables) o ingrese # para terminar el proceso: ")
                    if opcion_actualizar.lower() not in ["nombre", "quirofanos", "salas de espera", "consultorios", "direccion", "sillas", "camas", "ambulancias"]:
                        print("Ingrese una opcion valida")
                    else:
                        break
                opcion_actualizar = opcion_actualizar.lower()
                if opcion_actualizar == "nombre":
                    sede.nombre = input("Ingrese el nuevo nombre de la sede: ")
                if opcion_actualizar == "quirofanos":
                    sede.quirofanos = int(input("Ingrese la nueva cantidad de quirofanos de la sede: "))
                if opcion_actualizar == "salas de espera":
                    sede.salas_de_espera = int(input("Ingrese la nueva cantidad de salas de espera de la sede: "))
                if opcion_actualizar == "consultorios":
                    sede.consultorios = int(input("Ingrese la nueva cantidad de consultorios de la sede: "))
                if opcion_actualizar == "direccion":
                    sede.direccion = input("Ingrese la nueva direccion de la sede: ")
                if opcion_actualizar == "sillas":
                    sede.sillas = int(input("Ingrese la nueva cantidad de sillas de la sede: "))
                if opcion_actualizar == "camas":
                    sede.camas = int(input("Ingrese la nueva cantidad de camas de la sede: "))
                if opcion_actualizar == "ambulancias":
                    sede.ambulancias = int(input("Ingrese la nueva cantidad de ambulancias de la sede: "))
                if opcion_actualizar == "#":
                    Observacion.generar_observacion(cuenta, sede)
                    Gestor_Base.actualizar_objeto(sede, id)
                    print("Cambios realizados con exito!")
                    cls.editar_sede(cuenta)
        if opcion == 2:
            Cambiar_Estado.cambiar_estado(sede, cuenta, id)
            cls.editar_sede(cuenta)
        if opcion == 3:
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial_Administrativo(cuenta)



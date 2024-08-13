from src.ui_main.gestion_sedes.Editar_Sede import Editar_Sede
from src.ui_main.gestion_sedes.Ver_Lista_Sedes import Ver_Lista_Sedes
from src.ui_main.gestion_sedes.Ver_Sede import Ver_Sede


class Menu_Gestion_Sede:
    @classmethod
    def menu_gestion_sede(cls,cuenta):
        print("1. Editar Sede")
        print("2. Ver sede")
        print("3. Ver Lista de Sedes")
        print("4. Volver al menu principal")
        while True:
            try:
                opcion = int(input("Ingrese una opcion: "))
                if 1 <= opcion <= 4:
                    break
                else:
                    print("Ingrese un numero valido")
            except ValueError:
                print("Ingrese un numero")
        if opcion == 1:
            Editar_Sede.editar_sede(cuenta)
        if opcion == 2:
            Ver_Sede.ver_sede(cuenta)
        if opcion == 3:
            Ver_Lista_Sedes.ver_lista_sedes(cuenta)
        if opcion == 4:
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial_Administrativo(cuenta)
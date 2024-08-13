from src.ui_main.gestion_maestros.Crear_Maestro import Crear_Maestro
from src.ui_main.gestion_maestros.Editar_Maestro import Editar_Maestro
from src.ui_main.gestion_maestros.Ver_Lista_Maestros import Ver_Lista_Maestros
from src.ui_main.gestion_maestros.Ver_Maestro import Ver_Maestro


class Menu_Gestion_Maestros:
    @classmethod
    def menu_gestion_maestros(cls, cuenta):
        print("1. Crear Maestro")
        print("2. Editar Maestro")
        print("3. Ver Maestro")
        print("4. Ver Lista de Maestros")
        print("5. Volver al menu principal")
        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
                if 1 <= opcion <= 5:
                    break
                else:
                    print("Ingrese un numero dentro del rango")
            except ValueError:
                print("Ingrese un numero")
        if opcion == 1:
            Crear_Maestro.crear_maestro(cuenta)
        if opcion == 2:
            Editar_Maestro.editar_maestro(cuenta)
        if opcion == 3:
            Ver_Maestro.ver_maestro(cuenta)
        if opcion == 4:
            Ver_Lista_Maestros.ver_lista_maestros(cuenta)
        if opcion == 5:
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial_Administrativo(cuenta)

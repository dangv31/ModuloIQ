from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.Cambiar_Estado import Cambiar_Estado
from src.ui_main.gestion_cuentas.Editar_Datos_Basicos_Cuenta import Editar_Datos_Basicos_Cuenta
from src.ui_main.gestion_cuentas.Resetear_Contraseña import Resetear_Contrasena


class Editar_Cuenta:
    @classmethod
    def editar_cuenta(cls, cuenta):
        while True:
            try:
                doc = int(input("Ingrese el numero de documento de la cuenta: "))
                busqueda = Gestor_Base.buscar_objeto(doc, "Cuenta")
                if busqueda is None:
                    print("No existe una cuenta creada con este numero de documento")
                else:
                    break
            except ValueError:
                print("Error: Numero de documento debe ser un valor numérico. Intente de nuevo.")
        id, cuenta_e = Gestor_Base.buscar_objeto(doc, "Cuenta")
        print(cuenta_e.nombres)
        print(cuenta_e.apellidos)
        print(cuenta_e.doc)
        print()
        while True:
            print("Elija una de las siguientes opciones:")
            print("1. Editar Datos Basicos")
            print("2. Resetear contraseña")
            if cuenta_e.estado:
                print("3. Deshabilitar")
            else:
                print("3. Habilitar")

            print("4. Volver al menú principal")
            opcion = input()
            if opcion == "1":
                Editar_Datos_Basicos_Cuenta.editar_datos_basicos(cuenta_e, cuenta, id)
                break
            elif opcion == "2":
                Resetear_Contrasena.resetear_contrasena(cuenta_e, cuenta, id)
                break
            elif opcion == "3":
                Cambiar_Estado.cambiar_estado(cuenta_e, cuenta, id)
                break
            elif opcion == "4":
                from src.ui_main.Menu_inicial import Menu_inicial
                Menu_inicial.menu_inicial_Administrativo(cuenta)
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                print()

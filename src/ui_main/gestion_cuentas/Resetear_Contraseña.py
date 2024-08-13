from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Observacion import Observacion


class Resetear_Contrasena:
    @classmethod
    def resetear_contrasena(cls, cuenta_e, cuenta, id):
        while True:
            contrasena_nueva = input("Ingrese la nueva contraseña: ")
            confirmar_contrasena = input("Confirme la nueva contraseña: ")

            if contrasena_nueva == confirmar_contrasena:
                cuenta_e.contrasena = contrasena_nueva
                Observacion.generar_observacion(cuenta, cuenta_e)
                Gestor_Base.actualizar_objeto(cuenta_e, id)
                print("Cambio realizado con exito!")
                break
            else:
                print("Contraseñas no coinciden")

        from src.ui_main.Menu_inicial import Menu_inicial
        Menu_inicial.menu_inicial_Administrativo(cuenta)
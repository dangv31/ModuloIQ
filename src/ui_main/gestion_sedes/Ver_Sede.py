from src.base_datos.Gestor_Base import Gestor_Base


class Ver_Sede:
    @classmethod
    def ver_sede(cls, cuenta):
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
        print("Observaciones: ")
        for observacion in sede.observaciones:
            print(observacion)
        entrada = input("Ingrese cualquier caracter para volver al menu incial: ")
        if entrada:
            from src.ui_main.Menu_inicial import Menu_inicial
            if "Administrativo" in cuenta.rol:
                Menu_inicial.menu_inicial_Administrativo(cuenta)
            else:
                Menu_inicial.menu_inicial_Clinico(cuenta)

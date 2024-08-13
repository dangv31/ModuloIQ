from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Categoria import Categoria
from src.gestor_aplicacion.Observacion import Observacion
from src.ui_main.Cambiar_Estado import Cambiar_Estado


class Editar_Categorias:

    @classmethod
    def modificar_categoria(cls, maestro, cuenta, id):
        while True:
            if len(maestro.categorias) == 0:
                print("Este maestro no tiene categorias, por favor ingrese alguna")
                from src.ui_main.Menu_inicial import Menu_inicial
                return Menu_inicial.menu_inicial_Administrativo(cuenta)

            for index, categoria in enumerate(maestro.categorias):
                print(f"{index + 1}. {categoria}")
            while True:
                try:
                    opcion = int(input("Ingrese el indice de la categoria que desea modificar su informacion o 0 para finalizar el proceso: "))
                    if 0 <= opcion <= len(maestro.categorias):
                        break
                    else:
                        print("Ingrese un numero dentro del rango")
                except ValueError:
                    print("Ingrese un numero")
            if opcion == 0:
                break
            categoria_seleccionada = maestro.categorias[opcion - 1]
            for index, informacion in enumerate(categoria_seleccionada.info):
                print(f"{index + 1}. {informacion}")
            while True:
                try:
                    opcion_categoria = int(input("Ahora ingrese el indice de la información que desea cambiar: "))
                    if opcion_categoria <= len(categoria_seleccionada):
                        break
                    else:
                        print("Ingrese un numero dentro del rango")
                except ValueError:
                    print("Ingrese un numero")
            nueva_info = input("Ingrese la nueva informacion: ")
            categoria_seleccionada.actualizar_info(nueva_info, opcion_categoria - 1)
        Observacion.generar_observacion(cuenta, maestro)
        Gestor_Base.actualizar_objeto(maestro, id)
        print("Cambios realizados con exito!")
        return cls.editar_categorias(maestro, cuenta, id)

    @classmethod
    def editar_categorias(cls, maestro, cuenta, id):
        print("1. Modificar algun dato de una categoria")
        print("2. Deshabilitar o habilitar alguna categoria")
        print("3. Agregar una categoria")
        print("4. Volver al menu inicial")
        while True:
            try:
                opcion = int(input("Ingrese una opcion: "))
                if 1 <= opcion <= 4:
                    break
                else:
                    print("Ingrese un numero dentro del rango")
            except ValueError:
                print("Ingrese por favor un numero")
        if opcion == 1:
            return cls.modificar_categoria(maestro, cuenta, id)
        if opcion == 2:
            while True:
                while True:
                    for index, categoria in enumerate(maestro.categorias):
                        print(f"{index + 1}. {categoria}")
                    try:
                        opcion = int(input("Ingrese el indice de la categoria que desea habilitar o deshabilitar o # para finalizar el proceso: "))
                        if 1 <= opcion <= len(maestro.categorias):
                            break
                        else:
                            print("Ingrese un numero dentro del rango")
                    except ValueError:
                        print("Ingrese por favor un numero")
                if opcion == "#":
                    break
                categoria_seleccionada = maestro.categorias[opcion - 1]
                Cambiar_Estado.cambiar_estado(categoria_seleccionada, cuenta, id)
            Gestor_Base.actualizar_objeto(maestro, id)
            return cls.editar_categorias(maestro, cuenta, id)
        if opcion == 3:
            informacion = []
            for columna in maestro.columnas:
                print(columna)
                info = input("Ingrese la informacion de esta columna: ")
                informacion.append(info)
            Categoria(informacion, maestro)
            Gestor_Base.actualizar_objeto(maestro, id)
            return cls.editar_categorias(maestro, cuenta, id)
        if opcion == 4:
            from src.ui_main.Menu_inicial import Menu_inicial
            return Menu_inicial.menu_inicial_Administrativo(cuenta)

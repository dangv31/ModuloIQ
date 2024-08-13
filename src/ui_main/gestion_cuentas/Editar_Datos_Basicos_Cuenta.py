from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Observacion import Observacion


class Editar_Datos_Basicos_Cuenta:
    @classmethod
    def editar_datos_basicos(cls, cuenta_e, cuenta, id):

        global num_documento_nuevo
        while True:
            print("Seleccione la opcion que desea realizar: ")
            print("1. Cambiar nombre")
            print("2. Cambiar apellido")
            print("3. Cambiar numero de documento")
            print("4. Cambiar fecha de nacimiento")
            print("5. Cambiar correo")
            print("6. Cambiar rol")
            print("7. Cambiar sede")
            print("8. Volver al menu inicial")
            print()
            opcion = input()
            if opcion == "1":
                nombre_nuevo = input("Ingrese el nombre nuevo: ")
                cuenta_e.nombres = nombre_nuevo
                Observacion.generar_observacion(cuenta, cuenta_e)
                Gestor_Base.actualizar_objeto(cuenta_e, id)
                print("Cambio realizado con exito!")

            elif opcion == "2":
                apellido_nuevo = input("Ingrese el apellido nuevo: ")
                cuenta_e.apellidos = apellido_nuevo
                Observacion.generar_observacion(cuenta, cuenta_e)
                Gestor_Base.actualizar_objeto(cuenta_e, id)
                print("Cambio realizado con exito!")

            elif opcion == "3":
                while True:
                    try:
                        num_documento_nuevo = int(input("Ingrese el nuevo numero de documento: "))
                        busqueda = Gestor_Base.buscar_objeto(num_documento_nuevo, "Cuenta")
                        if busqueda is None:
                            break
                        else:
                            print("Ya hay una cuenta creada con este numero de documento")
                    except ValueError:
                        print("Error: Numero de documento debe ser un valor numérico. Intente de nuevo.")
                id, cuenta_e = Gestor_Base.buscar_objeto(num_documento_nuevo, "Cuenta")
                cuenta_e.doc = num_documento_nuevo
                Observacion.generar_observacion(cuenta, cuenta_e)
                Gestor_Base.actualizar_objeto(cuenta_e, id)
                print("Cambio realizado con exito!")

            elif opcion == "4":
                fecha_nacimiento_nueva = input("Ingrese la nueva fecha de nacimiento: ")
                cuenta_e.nacimiento = fecha_nacimiento_nueva
                Observacion.generar_observacion(cuenta, cuenta_e)
                Gestor_Base.actualizar_objeto(cuenta_e, id)
                print("Cambio realizado con exito!")

            elif opcion == "5":
                correo_nuevo = input("Ingrese el nuevo correo: ")
                cuenta_e.correo = correo_nuevo
                Observacion.generar_observacion(cuenta, cuenta_e)
                Gestor_Base.actualizar_objeto(cuenta_e, id)
                print("Cambio realizado con exito!")

            elif opcion == "6":
                while True:
                    print("1. Administrativo")
                    print("2. Clinico")
                    print("3. Administrativo-Clinico")
                    opc = input("Seleccione el rol que tendrá el usuario: ")
                    cuenta_e.rol.clear()
                    if opc in ["1", "2", "3"]:
                        if opc == "1" and "Administrativo" in cuenta.rol:
                            cuenta_e.rol.append("Administrativo")
                            break
                        elif opc == "2" and "Clinico" in cuenta.rol:
                            cuenta_e.rol.append("Clinico")
                            break
                        elif opc == "3" and "Administrativo" in cuenta.rol and "Clinico" in cuenta.rol:
                            cuenta_e.rol.append("Administrativo")
                            cuenta_e.rol.append("Clinico")
                            break
                        else:
                            print("no tienes permiso para crear una cuenta con este rol")
                            print()
                    else:
                        print("Error: Rol seleccionado no válido. Intente de nuevo.")

                Observacion.generar_observacion(cuenta, cuenta_e)
                Gestor_Base.actualizar_objeto(cuenta_e, id)
                print("Cambio realizado con exito!")

            elif opcion == "7":

                id_sede, sede = Gestor_Base.buscar_objeto("MedPLus Medellin", "Sede")
                if cuenta_e in sede.personal:
                    sede.personal.remove(cuenta_e)
                    Gestor_Base.actualizar_objeto(sede, id_sede)
                id_sede2, sede2 = Gestor_Base.buscar_objeto("MedPLus Manizales", "Sede")
                if cuenta_e in sede2.personal:
                    sede2.personal.remove(cuenta_e)
                    Gestor_Base.actualizar_objeto(sede2, id_sede2)
                id_sede3, sede3 = Gestor_Base.buscar_objeto("MedPLus Bogota", "Sede")
                if cuenta_e in sede3.personal:
                    sede3.personal.remove(cuenta_e)
                    Gestor_Base.actualizar_objeto(sede3, id_sede3)

                cuenta_e.sede.clear()

                while True:
                    print("1. Medellin")
                    print("2. Manizales")
                    print("3. Bogota")
                    print("4. Medellin-Manizales-Bogota")
                    opc = input("seleccione la sede en donde estara el usuario: ")
                    if opc == "1":
                        tiene_sede = False
                        for sed in cuenta.sede:
                            if sed.nombre == sede.nombre:
                                tiene_sede = True
                                break
                        if tiene_sede:
                            cuenta_e.sede.append(sede)
                            sede.personal.append(cuenta_e)
                            Gestor_Base.actualizar_objeto(sede, id_sede)
                            break
                    elif opc == "2":
                        tiene_sede = False
                        for sed in cuenta.sede:
                            if sed.nombre == sede2.nombre:
                                tiene_sede = True
                                break
                        if tiene_sede:
                            cuenta_e.sede.append(sede2)
                            sede2.personal.append(cuenta_e)
                            Gestor_Base.actualizar_objeto(sede2, id_sede2)
                            break
                    elif opc == "3":
                        tiene_sede = False
                        for sed in cuenta.sede:
                            if sed.nombre == sede3.nombre:
                                tiene_sede = True
                                break
                        if tiene_sede:
                            cuenta_e.sede.append(sede3)
                            sede3.personal.append(cuenta_e)
                            Gestor_Base.actualizar_objeto(sede3, id_sede3)
                            break
                    elif opc == "4":
                        tiene_sede = False
                        for sed in cuenta.sede:
                            if sed.nombre == sede.nombre or sed.nombre == sede2.nombre or sed.nombre == sede3.nombre:
                                tiene_sede += 1
                        if tiene_sede == 3:
                            cuenta_e.sede.append(sede)
                            sede.personal.append(cuenta_e)
                            Gestor_Base.actualizar_objeto(sede, id_sede)
                            cuenta_e.sede.append(sede2)
                            sede2.personal.append(cuenta_e)
                            Gestor_Base.actualizar_objeto(sede2, id_sede2)
                            cuenta_e.sede.append(sede3)
                            sede3.personal.append(cuenta_e)
                            Gestor_Base.actualizar_objeto(sede3, id_sede3)
                            break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")
                        print()

                Observacion.generar_observacion(cuenta, cuenta_e)
                Gestor_Base.actualizar_objeto(cuenta_e, id)
                print("Cambio realizado con exito!")

            elif opcion == "8":
                from src.ui_main.Menu_inicial import Menu_inicial
                Menu_inicial.menu_inicial_Administrativo(cuenta)
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
                print()

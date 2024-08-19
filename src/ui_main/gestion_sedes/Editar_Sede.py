from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Observacion import Observacion
from src.ui_main.Cambiar_Estado import Cambiar_Estado


import tkinter as tk
from tkinter import ttk, messagebox
from src.gestor_aplicacion.Sede import Sede
from src.ui_main.herramientas.volver_menu import volver_menu
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo

class Editar_Sede:
    @classmethod
    def editar_sede(cls, cuenta, ventana):
        def provisional():
            volver_menu(cuenta,ventana)

        def encontrar_sede():

            def actualizar_datos():

                def cambiar_nombre():
                    def actualizar(entrada):
                        sede.nombre = entrada.get()
                        def guardar_cambios_funcion():
                            from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                            Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "info")

                        for item in frame_info.winfo_children():
                            item.destroy()
                        sede.imprimir_info(frame_info)
                        for item in subframe.winfo_children():
                            item.destroy()

                        texto = tk.Label(subframe, text="Ingrese el nuevo nombre de la sede:")
                        texto.pack(pady=5)
                        entrada = tk.Entry(subframe)
                        entrada.pack(pady=5)
                        boton = tk.Button(subframe, text="Cambiar", command= lambda: actualizar(entrada))
                        boton.pack(side=tk.LEFT, padx=60)
                        guardar_cambios = tk.Button(subframe, text="Guardar Cambios", command= guardar_cambios_funcion)
                        guardar_cambios.pack(side=tk.LEFT, padx=60)

                    for item in subframe.winfo_children():
                        item.destroy()
                    texto = tk.Label(subframe, text="Ingrese el nuevo nombre de la sede:")
                    texto.pack(pady=5)
                    entrada = tk.Entry(subframe)
                    entrada.pack(pady=5)
                    boton = tk.Button(subframe, text="Cambiar", command= lambda:actualizar(entrada))
                    boton.pack(side=tk.LEFT, padx=60)
                
                def cambiar_quirofanos():
                    def actualizar(entrada):
                        sede.quirofanos = int(entrada.get())
                        def guardar_cambios_funcion():
                            from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                            Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "info")

                        for item in frame_info.winfo_children():
                            item.destroy()
                        sede.imprimir_info(frame_info)
                        for item in subframe.winfo_children():
                            item.destroy()

                        texto = tk.Label(subframe, text="Ingrese la nueva cantidad de quirofanos de la sede:")
                        texto.pack(pady=5)
                        entrada = tk.Entry(subframe)
                        entrada.pack(pady=5)
                        boton = tk.Button(subframe, text="Cambiar", command= lambda: actualizar(entrada))
                        boton.pack(side=tk.LEFT, padx=100)
                        guardar_cambios = tk.Button(subframe, text="Guardar Cambios", command= guardar_cambios_funcion)
                        guardar_cambios.pack(side=tk.LEFT, padx=60)

                    for item in subframe.winfo_children():
                        item.destroy()
                    texto = tk.Label(subframe, text="Ingrese la nueva cantidad de quirofanos de la sede:")
                    texto.pack(pady=5)
                    entrada = tk.Entry(subframe)
                    entrada.pack(pady=5)
                    boton = tk.Button(subframe, text="Cambiar", command= lambda: actualizar(entrada))
                    boton.pack(side=tk.LEFT, padx=100)
                
                def cambiar_salas():
                    def actualizar(entrada):
                        sede.salas_de_espera = int(entrada.get())
                        def guardar_cambios_funcion():
                            from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                            Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "info")

                        for item in frame_info.winfo_children():
                            item.destroy()
                        sede.imprimir_info(frame_info)
                        for item in subframe.winfo_children():
                            item.destroy()

                        texto = tk.Label(subframe, text="Ingrese la nueva cantidad de salas de espera de la sede:")
                        texto.pack(pady=5)
                        entrada = tk.Entry(subframe)
                        entrada.pack(pady=5)
                        boton = tk.Button(subframe, text="Cambiar", command= lambda: actualizar(entrada))
                        boton.pack(side=tk.LEFT, padx=140)
                        guardar_cambios = tk.Button(subframe, text="Guardar Cambios", command= guardar_cambios_funcion)
                        guardar_cambios.pack(side=tk.LEFT, padx=60)

                    for item in subframe.winfo_children():
                        item.destroy()
                    texto = tk.Label(subframe, text="Ingrese la nueva cantidad de salas de espera de la sede:")
                    texto.pack(pady=5)
                    entrada = tk.Entry(subframe)
                    entrada.pack(pady=5)
                    boton = tk.Button(subframe, text="Cambiar", command= lambda:actualizar(entrada))
                    boton.pack(side=tk.LEFT, padx=140)

                def cambiar_consultorios():
                    def actualizar(entrada):
                        sede.consultorios = int(entrada.get())
                        def guardar_cambios_funcion():
                            from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                            Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "info")

                        for item in frame_info.winfo_children():
                            item.destroy()
                        sede.imprimir_info(frame_info)
                        for item in subframe.winfo_children():
                            item.destroy()

                        texto = tk.Label(subframe, text="Ingrese la nueva cantidad de consultorios de la sede:")
                        texto.pack(pady=5)
                        entrada = tk.Entry(subframe)
                        entrada.pack(pady=5)
                        boton = tk.Button(subframe, text="Cambiar", command= lambda: actualizar(entrada))
                        boton.pack(side=tk.LEFT, padx=180)
                        guardar_cambios = tk.Button(subframe, text="Guardar Cambios", command= guardar_cambios_funcion)
                        guardar_cambios.pack(side=tk.LEFT, padx=60)

                    for item in subframe.winfo_children():
                        item.destroy()
                    texto = tk.Label(subframe, text="Ingrese la nueva cantidad de consultorios de la sede:")
                    texto.pack(pady=5)
                    entrada = tk.Entry(subframe)
                    entrada.pack(pady=5)
                    boton = tk.Button(subframe, text="Cambiar", command= lambda:actualizar(entrada))
                    boton.pack(side=tk.LEFT, padx=180)
                
                def cambiar_direccion():
                    def actualizar(entrada):
                        sede.direccion = entrada.get()
                        def guardar_cambios_funcion():
                            from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                            Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "info")

                        for item in frame_info.winfo_children():
                            item.destroy()
                        sede.imprimir_info(frame_info)
                        for item in subframe.winfo_children():
                            item.destroy()

                        texto = tk.Label(subframe, text="Ingrese la nueva direccion de la sede:")
                        texto.pack(pady=5)
                        entrada = tk.Entry(subframe)
                        entrada.pack(pady=5)
                        boton = tk.Button(subframe, text="Cambiar", command= lambda: actualizar(entrada))
                        boton.pack(side=tk.LEFT, padx=220)
                        guardar_cambios = tk.Button(subframe, text="Guardar Cambios", command= guardar_cambios_funcion)
                        guardar_cambios.pack(side=tk.LEFT, padx=60)

                    for item in subframe.winfo_children():
                        item.destroy()
                    texto = tk.Label(subframe, text="Ingrese la nueva direccion de la sede:")
                    texto.pack(pady=5)
                    entrada = tk.Entry(subframe)
                    entrada.pack(pady=5)
                    boton = tk.Button(subframe, text="Cambiar", command= lambda:actualizar(entrada))
                    boton.pack(side=tk.LEFT, padx=220)
                
                def cambiar_sillas():
                    def actualizar(entrada):
                        sede.sillas = int(entrada.get())
                        def guardar_cambios_funcion():
                            from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                            Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "info")

                        for item in frame_info.winfo_children():
                            item.destroy()
                        sede.imprimir_info(frame_info)
                        for item in subframe.winfo_children():
                            item.destroy()

                        texto = tk.Label(subframe, text="Ingrese la nueva cantidad de sillas de la sede:")
                        texto.pack(pady=5)
                        entrada = tk.Entry(subframe)
                        entrada.pack(pady=5)
                        boton = tk.Button(subframe, text="Cambiar", command= lambda: actualizar(entrada))
                        boton.pack(side=tk.LEFT, padx=260)
                        guardar_cambios = tk.Button(subframe, text="Guardar Cambios", command= guardar_cambios_funcion)
                        guardar_cambios.pack(side=tk.LEFT, padx=60)

                    for item in subframe.winfo_children():
                        item.destroy()
                    texto = tk.Label(subframe, text="Ingrese la nueva cantidad de sillas de la sede:")
                    texto.pack(pady=5)
                    entrada = tk.Entry(subframe)
                    entrada.pack(pady=5)
                    boton = tk.Button(subframe, text="Cambiar", command= lambda:actualizar(entrada))
                    boton.pack(side=tk.LEFT, padx=260)
                
                def cambiar_camas():
                    def actualizar(entrada):
                        sede.camas = int(entrada.get())
                        def guardar_cambios_funcion():
                            from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                            Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "info")

                        for item in frame_info.winfo_children():
                            item.destroy()
                        sede.imprimir_info(frame_info)
                        for item in subframe.winfo_children():
                            item.destroy()

                        texto = tk.Label(subframe, text="Ingrese la nueva cantidad de camas de la sede:")
                        texto.pack(pady=5)
                        entrada = tk.Entry(subframe)
                        entrada.pack(pady=5)
                        boton = tk.Button(subframe, text="Cambiar", command= lambda: actualizar(entrada))
                        boton.pack(side=tk.LEFT, padx=300)
                        guardar_cambios = tk.Button(subframe, text="Guardar Cambios", command= guardar_cambios_funcion)
                        guardar_cambios.pack(side=tk.LEFT, padx=60)

                    for item in subframe.winfo_children():
                        item.destroy()
                    texto = tk.Label(subframe, text="Ingrese la nueva cantidad de camas de la sede:")
                    texto.pack(pady=5)
                    entrada = tk.Entry(subframe)
                    entrada.pack(pady=5)
                    boton = tk.Button(subframe, text="Cambiar", command= lambda:actualizar(entrada))
                    boton.pack(side=tk.LEFT, padx=300)
                
                def cambiar_ambulancias():
                    def actualizar(entrada):
                        sede.ambulancias = int(entrada.get())
                        def guardar_cambios_funcion():
                            from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                            Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "info")

                        for item in frame_info.winfo_children():
                            item.destroy()
                        sede.imprimir_info(frame_info)
                        for item in subframe.winfo_children():
                            item.destroy()

                        texto = tk.Label(subframe, text="Ingrese la nueva cantidad de ambulancias de la sede:")
                        texto.pack(pady=5)
                        entrada = tk.Entry(subframe)
                        entrada.pack(pady=5)
                        boton = tk.Button(subframe, text="Cambiar", command= lambda: actualizar(entrada))
                        boton.pack(side=tk.LEFT, padx=360)
                        guardar_cambios = tk.Button(subframe, text="Guardar Cambios", command= guardar_cambios_funcion)
                        guardar_cambios.pack(side=tk.LEFT, padx=60)

                    for item in subframe.winfo_children():
                        item.destroy()
                    texto = tk.Label(subframe, text="Ingrese la nueva cantidad de ambulancias de la sede:")
                    texto.pack(pady=5)
                    entrada = tk.Entry(subframe)
                    entrada.pack(pady=5)
                    boton = tk.Button(subframe, text="Cambiar", command= lambda:actualizar(entrada))
                    boton.pack(side=tk.LEFT, padx=360)

                imprimir_titulo(ventana, "Elija los datos a cambiar:")

                frame_info = tk.Frame(ventana)
                frame_info.pack(pady=20)

                sede.imprimir_info(frame_info)

                frame_botones = tk.Frame(ventana)
                frame_botones.pack(pady=20)

                subframe = tk.Frame(frame_botones)
                subframe.pack(pady=20)

                nombre = tk.Button(frame_botones, text="Nombre", command= cambiar_nombre)
                nombre.pack(side=tk.LEFT, padx=5)

                quirofanos = tk.Button(frame_botones, text="Quirofanos", command= cambiar_quirofanos)
                quirofanos.pack(side=tk.LEFT, padx=5)

                salas = tk.Button(frame_botones, text="Salas De Espera",command= cambiar_salas)
                salas.pack(side=tk.LEFT, padx=5)

                consultorios = tk.Button(frame_botones, text="Consultorios", command= cambiar_consultorios)
                consultorios.pack(side=tk.LEFT, padx=5)

                direccion = tk.Button(frame_botones, text="Direccion", command= cambiar_direccion)
                direccion.pack(side=tk.LEFT, padx=5)

                sillas = tk.Button(frame_botones, text="Sillas", command= cambiar_sillas)
                sillas.pack(side=tk.LEFT, padx=5)

                camas = tk.Button(frame_botones, text="Camas", command= cambiar_camas)
                camas.pack(side=tk.LEFT, padx=5)
                
                ambulancias = tk.Button(frame_botones, text="Ambulancias", command= cambiar_ambulancias)
                ambulancias.pack(side=tk.LEFT, padx=5)

                volver = tk.Button(ventana, text="Volver", command= lambda: cls.editar_sede(cuenta,ventana))
                volver.pack(side=tk.LEFT, padx=600)

            busqueda = Gestor_Base.buscar_objeto(entrada_nombre.get(), "Sede")

            if busqueda is None:
                messagebox.showerror("Error", "Esta sede no existe.")
                return
            
            imprimir_titulo(ventana, "Elija una funcion:")
            id, sede = busqueda

            frame_info = tk.Frame(ventana)
            frame_info.pack(pady=20)

            sede.imprimir_info(frame_info)

            frame_botones = tk.Frame(ventana)
            frame_botones.pack(pady=20)

            actualizar = tk.Button(frame_botones, text="Actualizar datos basicos", command= actualizar_datos)
            actualizar.pack(side=tk.LEFT, padx=5)

            if sede.estado:
                from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                deshabilitar = tk.Button(frame_botones, text="Deshabilitar", command= lambda: Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "estado"))
                deshabilitar.pack(side=tk.LEFT, padx=5)
            else:
                from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
                habilitar = tk.Button(frame_botones, text="Habilitar", command= lambda: Interfaz_Observacion.generar_observacion(cuenta, sede, id, ventana, "estado"))
                habilitar.pack(side=tk.LEFT, padx=5)

            salir = tk.Button(frame_botones, text="Volver", command= lambda: cls.editar_sede(cuenta,ventana))
            salir.pack(side=tk.LEFT, padx=5)

        from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
        imprimir_titulo(ventana, "Buscar Sede:")

        frame_editar = tk.Frame(ventana)
        frame_editar.pack(pady=20)

        label_nombre = tk.Label(frame_editar, text="Ingrese el nombre de la Sede")
        label_nombre.pack(pady=5)

        entrada_nombre = tk.Entry(frame_editar)
        entrada_nombre.pack(pady=5)

        boton_buscar = tk.Button(frame_editar, text="Buscar Sede", command=encontrar_sede)
        boton_buscar.pack()

        salir = tk.Button(frame_editar, text="Volver al menu", command= provisional)
        salir.pack()



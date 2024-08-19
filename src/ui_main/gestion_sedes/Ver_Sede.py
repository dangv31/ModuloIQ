import tkinter as tk

from src.base_datos.Gestor_Base import Gestor_Base


class Ver_Sede:
    @classmethod
    def ver_sede(cls, cuenta, ventana):
        def provisional():
            volver_menu(cuenta,ventana)

        def buscar_sede():
            nombre_sede = entradaNombreSede.get()
            sede_1 = Gestor_Base.buscar_objeto(nombre_sede, "Sede")

            if sede_1 == None:
                tk.messagebox.showerror("Error", "Esta sede no existe.")
            else:
                for item in frame_info.winfo_children():
                    item.destroy()
                id = sede_1[0]
                sede = sede_1[1]
                sede.imprimir_info(frame_info)

                tk.Label(frame_info, text="Observaciones: ").pack()

                for observacion in sede.observaciones:
                    tk.Label(frame_info, text=observacion).pack()

        
        from src.ui_main.herramientas.volver_menu import volver_menu
        from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo

        imprimir_titulo(ventana, "Ver Sede:")

        frame_buscar = tk.Frame(ventana)
        frame_buscar.pack(pady=20)

        frame_info = tk.Frame(ventana)
        frame_info.pack(pady=20)

        textNombreSede = tk.Label(frame_buscar, text="Nombre De Sede:")
        textNombreSede.pack(pady=5)
        entradaNombreSede = tk.Entry(frame_buscar)
        entradaNombreSede.pack(pady=5)

        buscar = tk.Button(frame_buscar, text="Buscar", command= buscar_sede)
        buscar.pack(side=tk.TOP, padx=0)

        salir = tk.Button(ventana, text="Volver al menu", command= provisional)
        salir.pack(side=tk.LEFT, padx=600)

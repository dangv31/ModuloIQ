import tkinter as tk

from src.base_datos.Gestor_Base import Gestor_Base

class Ver_Lista_Sedes:
    @classmethod
    def ver_lista_sedes(cls, cuenta, ventana):
        from src.ui_main.herramientas.volver_menu import volver_menu
        from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
        lista_sedes = Gestor_Base.lista_sedes()

        def medellin_info():
            for item in frame_info.winfo_children():
                item.destroy()
            for id, sede in lista_sedes:
                if id == 1:
                    sede.imprimir_info(frame_info)

        def manizales_info():
            for item in frame_info.winfo_children():
                item.destroy()
            for id, sede in lista_sedes:
                if id == 2:
                    sede.imprimir_info(frame_info)

        def bogota_info():
            for item in frame_info.winfo_children():
                item.destroy()
            for id, sede in lista_sedes:
                if id == 3:
                    sede.imprimir_info(frame_info)
        def provisional():
            volver_menu(cuenta,ventana)

        imprimir_titulo(ventana, "Lista de Sedes:")

        frame_botones = tk.Frame(ventana)
        frame_botones.pack(pady=20)

        frame_info = tk.Frame(ventana)
        frame_info.pack(pady=20)

        medellin = tk.Button(frame_botones, text="Sede Medellín", command= medellin_info)
        manizales = tk.Button(frame_botones, text="Sede Manizales", command= manizales_info)
        bogota = tk.Button(frame_botones, text="Sede Bogotá", command= bogota_info)

        salir = tk.Button(frame_botones, text="Volver al menu", command= provisional)
        salir.pack(side=tk.LEFT, padx=5)


        medellin.pack(side=tk.LEFT, padx=5)
        manizales.pack(side=tk.LEFT, padx=5)
        bogota.pack(side=tk.LEFT, padx=5)

        salir.pack(side=tk.LEFT, padx=5)

import tkinter as tk
from tkinter import ttk, messagebox

from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.gestion_maestros.Crear_Maestro import Crear_Maestro

def buscar_maestro(ventana, cuenta):
    def encontrar_maestro():
        maestro_l = Gestor_Base.buscar_objeto(entrada_nombre.get(), "Maestro")
        if maestro_l is None:
            from src.ui_main.Menu_inicial import Menu_inicial
            if "Administrativo" in cuenta.rol:
                respuesta = messagebox.askyesno("Maestro no encontrado",
                                                "No existe el maestro. ¿Desea registrar un maestro?")
                if respuesta:
                    Crear_Maestro.crear_maestro(cuenta, ventana)
                else:
                    Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)
            else:
                messagebox.showerror("Error", "El maestro no existe.")
                Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)
            return
        return maestro_l
    from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
    imprimir_titulo(ventana, "Buscar maestro")
    frame = ttk.Frame(ventana)
    frame.pack()
    label_nombre = tk.Label(frame, text="Ingrese el nombre del maestro")
    label_nombre.pack(pady=5)
    entrada_nombre = tk.Entry(frame)
    entrada_nombre.pack(pady=5)
    boton_buscar = tk.Button(frame, text="Buscar maestro", command=encontrar_maestro)
    boton_buscar.pack()
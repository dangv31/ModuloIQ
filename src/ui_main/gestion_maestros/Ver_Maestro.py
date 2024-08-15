import tkinter as tk
from tkinter import messagebox, ttk

from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.gestion_maestros.Crear_Maestro import Crear_Maestro
from src.ui_main.herramientas.buscar_maestro import buscar_maestro
from src.ui_main.herramientas.volver_menu import volver_menu

class Ver_Maestro:
    @classmethod
    def ver_maestro(cls, cuenta, ventana):
        def encontrar_maestro():
            busqueda = Gestor_Base.buscar_objeto(entrada_nombre.get(), "Maestro")
            if busqueda is None:
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
            id, maestro=busqueda
            from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
            imprimir_titulo(ventana, maestro.nombre)
            frame = ttk.Frame(ventana)
            frame.pack()
            label_columna = tk.Label(frame, text="Columnas")
            label_columna.pack()
            frame_columnas = ttk.Frame(ventana)
            frame_columnas.pack()
            for index, col in enumerate(maestro.columnas):
                label_columna = tk.Label(frame_columnas, text=col)
                label_columna.grid(row=0, column=index)
            frame_categorias = ttk.Frame(ventana)
            frame_categorias.pack()
            label_categorias = tk.Label(frame_categorias, text="Categorias")
            label_categorias.pack()
            for index, categoria in enumerate(maestro.categorias):
                label_categoria = tk.Label(frame_categorias, text=categoria)
                label_categoria.pack()
            frame_observaciones = ttk.Frame(ventana)
            frame_observaciones.pack()
            for observacion in maestro.observaciones:
                label_observacion = tk.Label(frame_observaciones, text=observacion)
                label_observacion.pack()
            boton_volver = tk.Button(frame_observaciones, text="Volver", command=lambda: volver_menu(cuenta, ventana))
            boton_volver.pack()
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



import tkinter as tk
from tkinter import messagebox, ttk

from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.gestion_maestros.Crear_Maestro import Crear_Maestro
from src.ui_main.herramientas.volver_menu import volver_menu


class Ver_Lista_Maestros:
    @classmethod
    def ver_lista_maestros(cls, cuenta, ventana):
        # Limpiar la ventana para mostrar la lista de maestros
        for widget in ventana.winfo_children():
            widget.destroy()

        lista_maestros = Gestor_Base.lista_maestros()

        if len(lista_maestros) == 0:
            if "Administrativo" in cuenta.rol:
                respuesta = messagebox.askyesno("No hay maestros registrados",
                                                "¿Desea registrar algún maestro?")
                if respuesta:
                    Crear_Maestro.crear_maestro(cuenta, ventana)
                else:
                    cls.volver_menu(cuenta, ventana)
            else:
                messagebox.showinfo("Información", "No hay maestros registrados")
                cls.volver_menu(cuenta, ventana)
            return

        # Crear un canvas con scrollbar
        canvas = tk.Canvas(ventana)
        scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Empaquetar el canvas y scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Título
        label_titulo = tk.Label(scrollable_frame, text="Lista de Maestros", font=('Arial', 14, 'bold'))
        label_titulo.pack(pady=10)

        # Mostrar cada maestro
        for indice, (ID, maestro) in enumerate(lista_maestros, start=1):
            label_maestro = tk.Label(scrollable_frame, text=f"ID:{ID} - Maestro {indice}: {maestro.nombre}")
            label_maestro.pack(anchor="w", padx=10, pady=2)

            label_columnas = tk.Label(scrollable_frame, text="Columnas: " + ", ".join(maestro.columnas))
            label_columnas.pack(anchor="w", padx=20)

            label_cat = tk.Label(scrollable_frame, text="Categorias:")
            label_cat.pack(anchor="w", padx=20)
            for categoria in maestro.categorias:
                label_categorias = tk.Label(scrollable_frame, text=categoria)
                label_categorias.pack(anchor="w", padx=20)

            label_obs = tk.Label(scrollable_frame, text="Observaciones:")
            label_obs.pack(anchor="w", padx=20)
            label_observaciones = tk.Label(scrollable_frame, text=maestro.observaciones)
            label_observaciones.pack(anchor="w", padx=20)

            separator = ttk.Separator(scrollable_frame, orient='horizontal')
            separator.pack(fill=tk.X, pady=5)

        boton_volver = tk.Button(scrollable_frame, text="Volver al menú inicial",
                                 command=lambda: volver_menu(cuenta, ventana))
        boton_volver.pack(pady=20)

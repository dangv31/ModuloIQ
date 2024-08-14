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

        frame = ttk.Frame(ventana)
        frame.pack(fill=tk.BOTH, expand=True)

        # Título
        label_titulo = tk.Label(frame, text="Lista de Maestros", font=('Arial', 14, 'bold'))
        label_titulo.pack(pady=10)

        # Mostrar cada maestro
        for indice, (ID, maestro) in enumerate(lista_maestros, start=1):
            label_maestro = tk.Label(frame, text=f"ID:{ID} - Maestro {indice}: {maestro.nombre}", font=('Arial', 12))
            label_maestro.pack(anchor="w", padx=10, pady=2)

            label_columnas = tk.Label(frame, text="Columnas: " + ", ".join(maestro.columnas), font=('Arial', 10))
            label_columnas.pack(anchor="w", padx=20)
            label_cat = tk.Label(frame, text="Categorias:", font=('Arial', 10))
            label_cat.pack(anchor="w", padx=20)
            for categoria in maestro.categorias:
                label_categorias = tk.Label(frame, text=categoria, font=('Arial', 10))
                label_categorias.pack(anchor="w", padx=20)

            label_obs = tk.Label(frame, text="Observaciones:")
            label_obs.pack(anchor="w", padx=20)
            label_observaciones = tk.Label(frame, text=maestro.observaciones, font=('Arial', 10))
            label_observaciones.pack(anchor="w", padx=20)

            separator = ttk.Separator(frame, orient='horizontal')
            separator.pack(fill=tk.X, pady=5)

        boton_volver = tk.Button(frame, text="Volver al menú inicial", command=lambda: volver_menu(cuenta, ventana))
        boton_volver.pack(pady=20)
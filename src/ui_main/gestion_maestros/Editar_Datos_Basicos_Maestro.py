import tkinter as tk
from tkinter import ttk, messagebox

from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Observacion import Observacion
from src.ui_main.herramientas.volver_menu import volver_menu
from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion

class Editar_Datos_Basicos_Maestro:
    @classmethod
    def editar_datos_basicos(cls, maestro, cuenta, id, ventana):
        def cambiar_nombre():
            nombre_nuevo = entry_nombre.get()
            maestro.nombre = nombre_nuevo
            Interfaz_Observacion.generar_observacion(cuenta, maestro, id, ventana, maestro)
            # No cerramos la ventana principal, solo actualizamos la UI si es necesario

        def cambiar_nombre_columna():
            index_columna = int(combo_columnas.get().split('.')[0]) - 1
            nombre_col = entry_columna.get()
            maestro.columnas[index_columna] = nombre_col
            Interfaz_Observacion.generar_observacion(cuenta, maestro, id, ventana, maestro)
            # No cerramos la ventana principal, solo actualizamos la UI si es necesario

        from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
        imprimir_titulo(ventana, "Editar datos basicos de " + maestro.nombre)
        frame = ttk.Frame(ventana)
        frame.pack()
        lbl_opcion = tk.Label(frame, text="Seleccione la opción que desea realizar:")
        lbl_opcion.pack(pady=10)

        # Opción 1: Cambiar nombre
        label_nombre = tk.Label(frame, text="Ingresa el nuevo nombre")
        label_nombre.pack(pady=5)
        entry_nombre = tk.Entry(frame)
        entry_nombre.pack(pady=5)
        btn_cambiar_nombre = tk.Button(frame, text="Cambiar Nombre", command=lambda: cambiar_nombre())
        btn_cambiar_nombre.pack(pady=5)

        # Opción 2: Cambiar nombre de alguna columna
        label_col = tk.Label(frame, text="Elije una columna y escribe su nuevo nombre")
        label_col.pack(pady=5)
        columnas = maestro.columnas
        combo_columnas = ttk.Combobox(frame, values=[f"{i+1}. {columna}" for i, columna in enumerate(columnas)])
        combo_columnas.pack(pady=5)
        entry_columna = tk.Entry(frame)
        entry_columna.pack(pady=5)
        btn_cambiar_columna = tk.Button(frame, text="Cambiar Nombre de Columna", command=lambda: cambiar_nombre_columna())
        btn_cambiar_columna.pack(pady=5)

        # Opción 3: Volver al menú inicial
        btn_volver = tk.Button(frame, text="Volver al Menú Inicial", command=lambda: volver_menu(cuenta, ventana))
        btn_volver.pack(pady=10)
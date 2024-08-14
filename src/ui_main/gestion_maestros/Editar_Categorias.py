import tkinter as tk
from tkinter import ttk

from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Categoria import Categoria
from src.gestor_aplicacion.Observacion import Observacion
from src.ui_main.Cambiar_Estado import Cambiar_Estado
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo


class Editar_Categorias:

    @classmethod
    def modificar_categoria(cls, maestro, cuenta, id, ventana):
        imprimir_titulo(ventana, "Editar Categorias")
        frame = ttk.Frame(ventana)
        frame.pack()
        label_titulo=tk.Label(frame, text="Categorias del maestro " + maestro.nombre)
        label_titulo.pack()
        label_info = tk.Label(frame, text="Seleccione una categoria y la opción que desea realizar ")
        label_info.pack()
        frame_seleccion = tk.Frame(frame, bg="white")
        frame_seleccion.pack(fill="both", expand=True)
        listbox_categorias = tk.Listbox(frame_seleccion, bg="white")
        listbox_categorias.pack(fill="both", expand=True)
        for categoria in maestro.categorias:
            listbox_categorias.insert(tk.END, categoria)



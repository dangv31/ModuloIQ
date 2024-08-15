import tkinter as tk
from tkinter import ttk, messagebox

from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Categoria import Categoria
from src.gestor_aplicacion.Observacion import Observacion
from src.ui_main.Cambiar_Estado import Cambiar_Estado
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
from src.ui_main.herramientas.volver_menu import volver_menu
from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion

class Editar_Categorias:

    @classmethod
    def modificar_categoria(cls, maestro, cuenta, id, ventana):
        def editar_categoria():
            def actualizar_categoria():
                print(listbox_datos.curselection()[0])
                categoria_seleccionada.actualizar_info(entrada_dato.get(), listbox_datos.curselection()[0])
                Interfaz_Observacion.generar_observacion(cuenta, maestro, id, ventana, "info")

            categoria_seleccionada = maestro.categorias[listbox_categorias.curselection()[0]]
            imprimir_titulo(ventana, "Editar Categoria")
            frame_categorias = ttk.Frame(ventana)
            frame_categorias.pack()
            listbox_datos = tk.Listbox(frame_categorias, bg="white")
            listbox_datos.pack()
            label_seleccion = tk.Label(frame_categorias, text="Seleccione el dato a cambiar")
            label_seleccion.pack()
            for i, dato in enumerate(categoria_seleccionada.info):
                listbox_datos.insert(tk.END, f"{i + 1}. {dato}")
            label_dato = tk.Label(frame_categorias, text="Ingrese el nuevo dato")
            label_dato.pack()
            entrada_dato = tk.Entry(frame_categorias)
            entrada_dato.pack()

            boton_cambiar_dato = tk.Button(frame_categorias, text="Aplicar cambios", command=actualizar_categoria)
            boton_cambiar_dato.pack()
            boton_volver = tk.Button(frame_categorias, text="Cancelar",
                                     command=lambda: volver_menu(cuenta, ventana))
            boton_volver.pack()

        def estado_categoria():
            categoria_seleccionada = maestro.categorias[listbox_categorias.curselection()[0]]
            Interfaz_Observacion.generar_observacion(cuenta, [maestro, categoria_seleccionada], id, ventana, "estado_categoria")

        def agregar_categoria():
            def registrar_categoria():
                informacion = [entry.get() for entry in entry_info]
                nueva_categoria = Categoria(informacion, maestro)
                Gestor_Base.actualizar_objeto(maestro, id)
                messagebox.showinfo("Éxito", f"Categoría '{nueva_categoria}' agregada exitosamente.")
                from src.ui_main.Menu_inicial import Menu_inicial
                return Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)

            entry_info = []
            imprimir_titulo(ventana, f"Nueva categoria para {maestro.nombre}")
            frame = ttk.Frame(ventana)
            frame.pack()
            label_rellene = tk.Label(frame, text="Rellene la información de las columnas")
            label_rellene.pack()
            frame_campos = tk.Frame(ventana)
            frame_campos.pack()
            for i, columna in enumerate(maestro.columnas):
                label_col = tk.Label(frame_campos, text=f"{columna}: ")
                label_col.grid(row=i, column=0)
                entry_col = tk.Entry(frame_campos)
                entry_col.grid(row=i, column=1)
                entry_info.append(entry_col)
            frame2 = ttk.Frame(ventana)
            frame2.pack()
            boton_confirmar = tk.Button(frame2, text="Agregar categoria", command=registrar_categoria)
            boton_confirmar.pack()

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
        frame_botones = ttk.Frame(ventana)
        frame_botones.pack()
        boton_modificar = tk.Button(frame_botones, text="Modificar algun dato de una categoria", command=editar_categoria)
        boton_modificar.grid(row=0, column=0)
        boton_estado = tk.Button(frame_botones, text="Cambiar estado", command=estado_categoria)
        boton_estado.grid(row=0, column=1)
        boton_agregar = tk.Button(frame_botones, text="Agregar nueva categoria", command=agregar_categoria)
        boton_agregar.grid(row=0, column=2)
        boton_volver = tk.Button(frame_botones, text="Volver al menu inicial", command=lambda: volver_menu(cuenta, ventana))
        boton_volver.grid(row=0, column=3)



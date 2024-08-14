import tkinter as tk
from tkinter import messagebox
from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Maestro import Maestro
from src.ui_main.herramientas.volver_menu import volver_menu

class Crear_Maestro:
    @classmethod
    def crear_maestro(cls, cuenta, ventana):
        from src.ui_main.Menu_inicial import Menu_inicial
        from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
        imprimir_titulo(ventana, "Crear maestro")

        frame = tk.Frame(ventana)
        frame.pack(pady=20, padx=20)

        # Etiqueta y entrada para el nombre del maestro
        label_nombre = tk.Label(frame, text="Ingrese el nombre del maestro:")
        label_nombre.pack(pady=5)
        entrada_nombre = tk.Entry(frame)
        entrada_nombre.pack(pady=5)

        columnas = []

        def agregar_columna():
            nombre_col = entrada_columna.get()
            if nombre_col != "#":
                columnas.append(nombre_col)
                listbox.insert(tk.END, nombre_col)
                entrada_columna.delete(0, tk.END)

        def eliminar_columna():
            seleccion = listbox.curselection()
            if seleccion:
                index = seleccion[0]
                listbox.delete(index)
                columnas.pop(index)
            else:
                messagebox.showwarning("Advertencia", "Debe seleccionar una columna para eliminar.")

        def finalizar_creacion():
            nombre = entrada_nombre.get()
            busqueda = Gestor_Base.buscar_objeto(nombre, "Maestro")
            if busqueda is None:
                if columnas:
                    Gestor_Base.guardar_objeto(Maestro(nombre, columnas))
                    messagebox.showinfo("Éxito", f"¡Maestro '{nombre}' creado con éxito!")
                    Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)
                else:
                    messagebox.showwarning("Advertencia", "Debe agregar al menos una columna.")
            else:
                messagebox.showerror("Error", "Ya existe un maestro con ese nombre.")
                Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)

        # Botón para agregar una nueva columna
        label_nombre_col = tk.Label(frame, text="Ingrese el nombre de las columnas y oprima Enter o el boton Agregar columna:")
        label_nombre_col.pack(pady=5)
        entrada_columna = tk.Entry(frame)
        entrada_columna.pack(pady=5)

        boton_agregar = tk.Button(frame, text="Agregar Columna", command=agregar_columna)
        boton_agregar.pack(pady=5)

        # Listbox para mostrar las columnas agregadas
        listbox = tk.Listbox(frame)
        listbox.pack(pady=5)

        # Botón para eliminar una columna seleccionada
        boton_eliminar = tk.Button(frame, text="Eliminar Columna", command=eliminar_columna)
        boton_eliminar.pack(pady=5)

        # Botón para finalizar la creación del maestro
        boton_finalizar = tk.Button(frame, text="Finalizar Creación", command=finalizar_creacion)
        boton_finalizar.pack(pady=20)

        # Botón para cancelar creacion de maestro
        boton_cancelar = tk.Button(frame, text="Cancelar", command=lambda: volver_menu(cuenta, ventana))
        boton_cancelar.pack()

        def on_enter(event):
            agregar_columna()

        entrada_columna.bind("<Return>", on_enter)  # Permite añadir columnas con Enter


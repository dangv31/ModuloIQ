import tkinter as tk
from tkinter import ttk, messagebox
from src.gestor_aplicacion.Observacion import Observacion
from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
from src.ui_main.herramientas.volver_menu import volver_menu
from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion

class Editar_Datos_Basicos_Cuenta:
    @classmethod
    def editar_datos_basicos(cls, cuenta_e, cuenta, id, ventana):
        def cambiar_nombre():
            nombre_nuevo = entry_nombre.get()
            cuenta_e.nombres = nombre_nuevo
            Interfaz_Observacion.generar_observacion(cuenta, cuenta_e, id, ventana, "info")

        def cambiar_apellido():
            apellido_nuevo = entry_apellido.get()
            cuenta_e.apellidos = apellido_nuevo
            Interfaz_Observacion.generar_observacion(cuenta, cuenta_e, id, ventana, "info")

        def cambiar_num_documento():
            try:
                num_documento_nuevo = int(entry_documento.get())
                cuenta_e.doc = num_documento_nuevo
                Interfaz_Observacion.generar_observacion(cuenta, cuenta_e, id, ventana, "info")
            except ValueError:
                messagebox.showerror("Error", "Número de documento debe ser numérico.")

        def cambiar_fecha_nacimiento():
            fecha_nacimiento_nueva = entry_nacimiento.get()
            cuenta_e.nacimiento = fecha_nacimiento_nueva
            Interfaz_Observacion.generar_observacion(cuenta, cuenta_e, id, ventana, "info")

        def cambiar_correo():
            correo_nuevo = entry_correo.get()
            cuenta_e.correo = correo_nuevo
            Interfaz_Observacion.generar_observacion(cuenta, cuenta_e, id, ventana, "info")

        imprimir_titulo(ventana, "Editar datos básicos de la cuenta")

        frame = ttk.Frame(ventana)
        frame.pack()

        # Opción para cambiar nombre
        label_nombre = tk.Label(frame, text="Ingresa el nuevo nombre:")
        label_nombre.pack(pady=5)
        entry_nombre = tk.Entry(frame)
        entry_nombre.pack(pady=5)
        btn_cambiar_nombre = tk.Button(frame, text="Cambiar Nombre", command=cambiar_nombre)
        btn_cambiar_nombre.pack(pady=5)

        # Opción para cambiar apellido
        label_apellido = tk.Label(frame, text="Ingresa el nuevo apellido:")
        label_apellido.pack(pady=5)
        entry_apellido = tk.Entry(frame)
        entry_apellido.pack(pady=5)
        btn_cambiar_apellido = tk.Button(frame, text="Cambiar Apellido", command=cambiar_apellido)
        btn_cambiar_apellido.pack(pady=5)

        # Opción para cambiar número de documento
        label_documento = tk.Label(frame, text="Ingresa el nuevo número de documento:")
        label_documento.pack(pady=5)
        entry_documento = tk.Entry(frame)
        entry_documento.pack(pady=5)
        btn_cambiar_documento = tk.Button(frame, text="Cambiar Número de Documento", command=cambiar_num_documento)
        btn_cambiar_documento.pack(pady=5)

        # Opción para cambiar fecha de nacimiento
        label_nacimiento = tk.Label(frame, text="Ingresa la nueva fecha de nacimiento:")
        label_nacimiento.pack(pady=5)
        entry_nacimiento = tk.Entry(frame)
        entry_nacimiento.pack(pady=5)
        btn_cambiar_nacimiento = tk.Button(frame, text="Cambiar Fecha de Nacimiento", command=cambiar_fecha_nacimiento)
        btn_cambiar_nacimiento.pack(pady=5)

        # Opción para cambiar correo
        label_correo = tk.Label(frame, text="Ingresa el nuevo correo:")
        label_correo.pack(pady=5)
        entry_correo = tk.Entry(frame)
        entry_correo.pack(pady=5)
        btn_cambiar_correo = tk.Button(frame, text="Cambiar Correo", command=cambiar_correo)
        btn_cambiar_correo.pack(pady=5)

        # Opción para volver al menú inicial
        btn_volver = tk.Button(frame, text="Volver al Menú Inicial", command=lambda: volver_menu(cuenta, ventana))
        btn_volver.pack(pady=10)
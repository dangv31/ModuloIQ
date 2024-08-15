import tkinter as tk
from tkinter import messagebox, ttk
from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Observacion import Observacion
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
from src.ui_main.herramientas.volver_menu import volver_menu


class Resetear_Contrasena:
    @classmethod
    def resetear_contrasena(cls, cuenta_e, cuenta, id, ventana):
        def confirmar_reset():
            contrasena_nueva = entry_contrasena.get()
            confirmar_contrasena = entry_confirmar_contrasena.get()

            if contrasena_nueva == confirmar_contrasena:
                cuenta_e.contrasena = contrasena_nueva
                Interfaz_Observacion.generar_observacion(cuenta, cuenta_e, id, ventana, "info")

            else:
                messagebox.showerror("Error", "Las contraseñas no coinciden. Intente de nuevo.")

        imprimir_titulo(ventana, "Editar contraseña")

        frame = ttk.Frame(ventana)
        frame.pack()

        # Campo para ingresar la nueva contraseña
        label_contrasena = tk.Label(frame, text="Ingrese la nueva contraseña:")
        label_contrasena.pack(pady=5)
        entry_contrasena = tk.Entry(frame, show="*")  # Campo de entrada para la contraseña con máscara
        entry_contrasena.pack(pady=5)

        # Campo para confirmar la nueva contraseña
        label_confirmar_contrasena = tk.Label(frame, text="Confirme la nueva contraseña:")
        label_confirmar_contrasena.pack(pady=5)
        entry_confirmar_contrasena = tk.Entry(frame, show="*")  # Campo de entrada para la confirmación con máscara
        entry_confirmar_contrasena.pack(pady=5)

        # Botón para confirmar el cambio de contraseña
        btn_confirmar = tk.Button(frame, text="Confirmar", command=confirmar_reset)
        btn_confirmar.pack(pady=10)

        # Botón para volver al menú inicial
        btn_volver = tk.Button(frame, text="Volver al Menú Inicial", command=lambda: volver_menu(cuenta, ventana))
        btn_volver.pack(pady=10)
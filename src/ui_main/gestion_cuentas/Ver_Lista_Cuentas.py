import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.herramientas.volver_menu import volver_menu

class Ver_Lista_Cuentas:
    @classmethod
    def ver_lista_cuentas(cls, cuenta_principal, ventana):
        # Limpiar la ventana para mostrar la lista de cuentas
        for widget in ventana.winfo_children():
            widget.destroy()

        lista_cuentas = Gestor_Base.lista_cuentas()

        if len(lista_cuentas) == 0:
            messagebox.showinfo("Información", "No hay cuentas registradas")
            volver_menu(cuenta_principal, ventana)
            return

        frame = ttk.Frame(ventana)
        frame.pack(fill=tk.BOTH, expand=True)

        # Título
        label_titulo = tk.Label(frame, text="Lista de Cuentas", font=('Arial', 14, 'bold'))
        label_titulo.pack(pady=10)

        # Mostrar cada cuenta
        for indice, (ID, cuenta) in enumerate(lista_cuentas, start=1):
            label_cuenta = tk.Label(frame, text=f"Cuenta {indice}: {cuenta.nombres} {cuenta.apellidos}", font=('Arial', 12))
            label_cuenta.pack(anchor="w", padx=10, pady=2)

            label_doc = tk.Label(frame, text=f"Número de Documento: {cuenta.doc}", font=('Arial', 10))
            label_doc.pack(anchor="w", padx=20)

            label_correo = tk.Label(frame, text=f"Correo: {cuenta.correo}", font=('Arial', 10))
            label_correo.pack(anchor="w", padx=20)

            label_rol = tk.Label(frame, text="Roles: " + ", ".join(cuenta.rol), font=('Arial', 10))
            label_rol.pack(anchor="w", padx=20)

            label_estado = tk.Label(frame, text=f"Estado: {'Habilitada' if cuenta.estado else 'Deshabilitada'}", font=('Arial', 10))
            label_estado.pack(anchor="w", padx=20)

            label_sedes = tk.Label(frame, text="Sedes: " + ", ".join([sede.nombre for sede in cuenta.sede]), font=('Arial', 10))
            label_sedes.pack(anchor="w", padx=20)

            label_obs = tk.Label(frame, text="Observaciones:")
            label_obs.pack(anchor="w", padx=20)
            label_observaciones = tk.Label(frame, text=cuenta.observaciones, font=('Arial', 10))
            label_observaciones.pack(anchor="w", padx=20)
            
            separator = ttk.Separator(frame, orient='horizontal')
            separator.pack(fill=tk.X, pady=5)

        # Botón para volver al menú inicial
        boton_volver = tk.Button(frame, text="Volver al menú principal", command=lambda: volver_menu(cuenta_principal, ventana))
        boton_volver.pack(pady=20)
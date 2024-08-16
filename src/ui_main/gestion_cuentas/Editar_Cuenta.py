import tkinter as tk
from tkinter import messagebox, ttk

from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.gestion_cuentas.Editar_Datos_Basicos_Cuenta import Editar_Datos_Basicos_Cuenta
from src.ui_main.gestion_cuentas.Resetear_Contrasena import Resetear_Contrasena
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
from src.ui_main.herramientas.volver_menu import volver_menu

class Editar_Cuenta:
    @classmethod
    def editar_cuenta(cls, cuenta, ventana):
        def encontrar_cuenta():
            try:
                doc = int(entrada_doc.get())
                busqueda = Gestor_Base.buscar_objeto(doc, "Cuenta")
                if busqueda is None:
                    messagebox.showerror("Error", "No existe una cuenta con este número de documento.")
                    return
            except ValueError:
                messagebox.showerror("Error", "El número de documento debe ser un valor numérico.")
                return

            id, cuenta_e = busqueda
            estado = "Habilitada" if cuenta_e.estado else "Deshabilitada"
            imprimir_titulo(ventana, f"Editar {cuenta_e.nombres} {cuenta_e.apellidos} - Estado: {estado}")

            # Crear un frame para los botones de opciones
            frame_opciones = ttk.Frame(ventana)
            frame_opciones.pack(pady=20)

            label_opcion = tk.Label(frame_opciones, text="Seleccione una opción:")
            label_opcion.pack(pady=10)

            boton_datos = tk.Button(frame_opciones, text="Editar Datos Básicos", 
                                    command=lambda: Editar_Datos_Basicos_Cuenta.editar_datos_basicos(cuenta_e, cuenta, id, ventana))
            boton_datos.pack(pady=10)

            boton_contrasena = tk.Button(frame_opciones, text="Resetear Contraseña", 
                                         command=lambda: Resetear_Contrasena.resetear_contrasena(cuenta_e, cuenta, id, ventana))
            boton_contrasena.pack(pady=10)

            if cuenta_e.estado:
                boton_estado = tk.Button(frame_opciones, text="Deshabilitar Cuenta", 
                                         command=lambda: Interfaz_Observacion.generar_observacion(cuenta, cuenta_e, id, ventana, "estado"))
            else:
                boton_estado = tk.Button(frame_opciones, text="Habilitar Cuenta", 
                                         command=lambda: Interfaz_Observacion.generar_observacion(cuenta, cuenta_e, id, ventana, "estado"))
            boton_estado.pack(pady=10)

            boton_volver = tk.Button(frame_opciones, text="Volver al Menú Principal", 
                                     command=lambda: volver_menu(cuenta, ventana))
            boton_volver.pack(pady=20)

        # Limpiar la ventana para mostrar la interfaz de búsqueda
        for widget in ventana.winfo_children():
            widget.destroy()

        imprimir_titulo(ventana, "Buscar Cuenta")
        frame = ttk.Frame(ventana)
        frame.pack(pady=20)

        label_doc = tk.Label(frame, text="Ingrese el número de documento:")
        label_doc.pack(pady=5)

        entrada_doc = tk.Entry(frame)
        entrada_doc.pack(pady=5)

        boton_buscar = tk.Button(frame, text="Buscar Cuenta", command=encontrar_cuenta)
        boton_buscar.pack(pady=10)
import tkinter as tk
from tkinter import messagebox, ttk
from src.base_datos.Gestor_Base import Gestor_Base

class Ver_Cuenta:
    @classmethod
    def ver_cuenta(cls, cuenta_principal, ventana):
        def encontrar_cuenta():
            try:
                doc = int(entrada_doc.get())
                busqueda = Gestor_Base.buscar_objeto(doc, "Cuenta")
                if busqueda is None:
                    from src.ui_main.Menu_inicial import Menu_inicial
                    respuesta = messagebox.askyesno("Cuenta no encontrada",
                                                    "No existe una cuenta con este número de documento. ¿Desea crear una nueva cuenta?")
                    if respuesta:
                        from src.ui_main.gestion_cuentas.Crear_Cuenta import Crear_Cuenta
                        Crear_Cuenta.crear_cuenta(cuenta_principal, ventana)
                    else:
                        Menu_inicial.menu_inicial_Administrativo(cuenta_principal, ventana)
                else:
                    mostrar_detalles(busqueda[1])
            except ValueError:
                messagebox.showerror("Error", "El número de documento debe ser un valor numérico.")

        def mostrar_detalles(cuenta):
            from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
            imprimir_titulo(ventana, f"Cuenta de {cuenta.nombres} {cuenta.apellidos}")

            frame = ttk.Frame(ventana)
            frame.pack()

            # Detalles de la cuenta
            detalles = [
                ("Nombre:", cuenta.nombres),
                ("Apellido:", cuenta.apellidos),
                ("Número de documento:", cuenta.doc),
                ("Fecha de nacimiento:", cuenta.nacimiento),
                ("Correo:", cuenta.correo),
                ("Rol:", ", ".join(cuenta.rol)),
                ("Estado:", "Habilitada" if cuenta.estado else "Deshabilitada"),
                ("Sede:", ", ".join([sede.nombre for sede in cuenta.sede]))
            ]

            for label_text, valor in detalles:
                frame_detalle = ttk.Frame(ventana)
                frame_detalle.pack(anchor="w", padx=10, pady=2)
                label = tk.Label(frame_detalle, text=label_text)
                label.pack(side="left")
                label_valor = tk.Label(frame_detalle, text=valor)
                label_valor.pack(side="left")

            # Botón para regresar al menú principal
            boton_volver = tk.Button(ventana, text="Volver al menú principal",
                                     command=lambda: volver_menu(cuenta_principal, ventana))
            boton_volver.pack(pady=20)

        # Configuración inicial
        from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
        imprimir_titulo(ventana, "Buscar cuenta")

        frame = ttk.Frame(ventana)
        frame.pack()

        label_doc = tk.Label(frame, text="Ingrese el número de documento de la cuenta:")
        label_doc.pack(pady=5)
        entrada_doc = tk.Entry(frame)
        entrada_doc.pack(pady=5)

        boton_buscar = tk.Button(frame, text="Buscar cuenta", command=encontrar_cuenta)
        boton_buscar.pack(pady=10)

        # Botón para regresar al menú principal
        boton_volver = tk.Button(frame, text="Volver al menú principal",
                                 command=lambda: volver_menu(cuenta_principal, ventana))
        boton_volver.pack(pady=10)

def volver_menu(cuenta, ventana):
    from src.ui_main.Menu_inicial import Menu_inicial
    Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)
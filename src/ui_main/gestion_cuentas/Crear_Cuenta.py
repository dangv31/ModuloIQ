import tkinter as tk
from tkinter import messagebox
from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Cuenta import Cuenta
from src.ui_main.herramientas.volver_menu import volver_menu

class Crear_Cuenta:
    @classmethod
    def crear_cuenta(cls, cuenta, ventana):
        from src.ui_main.Menu_inicial import Menu_inicial
        from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
        imprimir_titulo(ventana, "Crear Cuenta")

        frame = tk.Frame(ventana)
        frame.pack(pady=20, padx=20)

        # Función para verificar el documento
        def verificar_documento():
            try:
                doc = int(entrada_doc.get())
                busqueda = Gestor_Base.buscar_objeto(doc, "Cuenta")
                if busqueda is None:
                    return doc
                else:
                    messagebox.showerror("Error", "Ya existe una cuenta con este número de documento.")
            except ValueError:
                messagebox.showerror("Error", "El número de documento debe ser un valor numérico.")

        def finalizar_creacion():
            nombre = entrada_nombre.get().strip()
            apellido = entrada_apellido.get().strip()
            doc = verificar_documento()
            nacimiento = entrada_nacimiento.get().strip()
            correo = entrada_correo.get().strip()
            contrasena = entrada_contrasena.get().strip()

            # Verificar si algún campo está vacío
            if not nombre or not apellido or not doc or not nacimiento or not correo or not contrasena:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            if doc is None:
                return

            cuenta_creada = Cuenta(nombre, apellido, doc, nacimiento, correo, contrasena)

            rol = rol_var.get()
            sede = sede_var.get()

            if rol == "Administrativo" and "Administrativo" in cuenta.rol:
                cuenta_creada.rol.append("Administrativo")
            elif rol == "Clinico" and "Clinico" in cuenta.rol:
                cuenta_creada.rol.append("Clinico")
            elif rol == "Administrativo-Clinico" and "Administrativo" in cuenta.rol and "Clinico" in cuenta.rol:
                cuenta_creada.rol.append("Administrativo")
                cuenta_creada.rol.append("Clinico")
            else:
                messagebox.showerror("Error", "No tienes permiso para asignar este rol.")
                return

            if sede == "Medellin" or sede == "Medellin-Manizales-Bogota":
                id_sede, sede_obj = Gestor_Base.buscar_objeto("MedPLus Medellin", "Sede")
                cuenta_creada.sede.append(sede_obj)
                sede_obj.personal.append(cuenta_creada)
                Gestor_Base.actualizar_objeto(sede_obj, id_sede)

            if sede == "Manizales" or sede == "Medellin-Manizales-Bogota":
                id_sede, sede_obj = Gestor_Base.buscar_objeto("MedPLus Manizales", "Sede")
                cuenta_creada.sede.append(sede_obj)
                sede_obj.personal.append(cuenta_creada)
                Gestor_Base.actualizar_objeto(sede_obj, id_sede)

            if sede == "Bogota" or sede == "Medellin-Manizales-Bogota":
                id_sede, sede_obj = Gestor_Base.buscar_objeto("MedPLus Bogota", "Sede")
                cuenta_creada.sede.append(sede_obj)
                sede_obj.personal.append(cuenta_creada)
                Gestor_Base.actualizar_objeto(sede_obj, id_sede)

            Gestor_Base.guardar_objeto(cuenta_creada)
            messagebox.showinfo("Éxito", "¡Cuenta creada con éxito!")
            Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)

        # Etiquetas y entradas para la información de la cuenta
        label_nombre = tk.Label(frame, text="Nombre:")
        label_nombre.pack(pady=5)
        entrada_nombre = tk.Entry(frame)
        entrada_nombre.pack(pady=5)

        label_apellido = tk.Label(frame, text="Apellido:")
        label_apellido.pack(pady=5)
        entrada_apellido = tk.Entry(frame)
        entrada_apellido.pack(pady=5)

        label_doc = tk.Label(frame, text="Número de documento:")
        label_doc.pack(pady=5)
        entrada_doc = tk.Entry(frame)
        entrada_doc.pack(pady=5)

        label_nacimiento = tk.Label(frame, text="Fecha de nacimiento (DD/MM/AAAA):")
        label_nacimiento.pack(pady=5)
        entrada_nacimiento = tk.Entry(frame)
        entrada_nacimiento.pack(pady=5)

        label_correo = tk.Label(frame, text="Correo:")
        label_correo.pack(pady=5)
        entrada_correo = tk.Entry(frame)
        entrada_correo.pack(pady=5)

        label_contrasena = tk.Label(frame, text="Contraseña:")
        label_contrasena.pack(pady=5)
        entrada_contrasena = tk.Entry(frame, show="*")
        entrada_contrasena.pack(pady=5)

        # Menú desplegable para seleccionar el rol
        label_rol = tk.Label(frame, text="Seleccione el rol:")
        label_rol.pack(pady=5)
        rol_var = tk.StringVar(frame)
        rol_var.set("Administrativo")  # valor por defecto
        roles = ["Administrativo", "Clinico", "Administrativo-Clinico"]
        rol_menu = tk.OptionMenu(frame, rol_var, *roles)
        rol_menu.pack(pady=5)

        # Menú desplegable para seleccionar la sede
        label_sede = tk.Label(frame, text="Seleccione la sede:")
        label_sede.pack(pady=5)
        sede_var = tk.StringVar(frame)
        sede_var.set("Medellin")  # valor por defecto
        sedes = ["Medellin", "Manizales", "Bogota", "Medellin-Manizales-Bogota"]
        sede_menu = tk.OptionMenu(frame, sede_var, *sedes)
        sede_menu.pack(pady=5)

        # Botón para finalizar la creación de la cuenta
        boton_finalizar = tk.Button(frame, text="Finalizar Creación", command=finalizar_creacion)
        boton_finalizar.pack(pady=20)

        # Botón para cancelar la creación de la cuenta
        boton_cancelar = tk.Button(frame, text="Cancelar", command=lambda: volver_menu(cuenta, ventana))
        boton_cancelar.pack()
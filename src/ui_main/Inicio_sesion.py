from tkinter import messagebox, ttk
import tkinter as tk

from herramientas.imprimir_titulo import imprimir_titulo
from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.Menu_inicial import Menu_inicial

class Inicio_sesion:

    @classmethod
    def inicio_sesion(cls, ventana):
        def verificar_credenciales():
            correo_ingresado = entrada_correo.get()
            contrasena_ingresada = entrada_contraseña.get()
            cuenta_encontrada = None
            lista_cuentas = Gestor_Base.lista_cuentas()

            for id, cuenta in lista_cuentas:
                if cuenta.correo == correo_ingresado and cuenta.contrasena == contrasena_ingresada:
                    cuenta_encontrada = cuenta
                    break
            if cuenta_encontrada:
                if cuenta_encontrada.estado:
                    if "Administrativo" in cuenta_encontrada.rol:
                        print()
                        print(f"¡Bienvenido {cuenta_encontrada.nombres}!")
                        Menu_inicial.menu_inicial_Administrativo(cuenta_encontrada, ventana)
                    else:
                        print()
                        print(f"¡Bienvenido {cuenta_encontrada.nombres}!")
                        Menu_inicial.menu_inicial_Clinico(cuenta_encontrada, ventana)
                else:
                    respuesta = messagebox.askyesno("Cuenta deshabilitada", "Esta cuenta está deshabilitada. ¿Deseas cerrar la aplicación?")
                    if respuesta:
                        ventana.destroy()  # Cerrar la aplicación
                    else:
                        Inicio_sesion.inicio_sesion(ventana)

            else:
                respuesta = messagebox.askyesno("Cuenta no existe",
                                                "Esta cuenta no existe. ¿Deseas cerrar la aplicación?")
                if respuesta:
                    ventana.destroy()  # Cerrar la aplicación
                else:
                    Inicio_sesion.inicio_sesion(ventana)
        imprimir_titulo(ventana, "Inicio Sesion")
        frame = ttk.Frame(ventana)
        frame.pack()
        etiqueta_correo = tk.Label(frame, text="Usuario:")
        etiqueta_correo.pack(pady=5)

        entrada_correo = tk.Entry(frame)
        entrada_correo.pack(pady=5)

        etiqueta_contraseña = tk.Label(frame, text="Contraseña:")
        etiqueta_contraseña.pack(pady=5)

        entrada_contraseña = tk.Entry(frame, show="*")
        entrada_contraseña.pack(pady=5)

        # Botón de inicio de sesión
        boton_login = tk.Button(frame, text="Iniciar sesión", command=verificar_credenciales)
        boton_login.pack(pady=20)
import tkinter as tk
from tkinter import ttk
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
from src.ui_main.gestion_maestros.Crear_Maestro import Crear_Maestro
from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Cuenta import Cuenta
from src.gestor_aplicacion.Sede import Sede
from src.ui_main.gestion_cuentas.Menu_Gestion_Cuentas import Menu_Gestion_Cuentas
from src.ui_main.gestion_maestros.Menu_Gestion_Maestros import Menu_Gestion_Maestros
from src.ui_main.gestion_maestros.Ver_Lista_Maestros import Ver_Lista_Maestros
from src.ui_main.gestion_maestros.Ver_Maestro import Ver_Maestro
from src.ui_main.gestion_sedes.Menu_Gestion_Sede import Menu_Gestion_Sede
from src.ui_main.gestion_sedes.Ver_Lista_Sedes import Ver_Lista_Sedes
from src.ui_main.gestion_sedes.Ver_Sede import Ver_Sede

class Menu_inicial:
    @classmethod
    def menu_inicial_Administrativo(cls, cuenta, frame):
        imprimir_titulo(frame, "Menu Inicial Administrativo")
        frame_inicial = ttk.Frame()
        frame_inicial.pack(fill=tk.BOTH, expand=1)
        label_info = ttk.Label(frame_inicial, text="Bienvenido por favor selecciona en el menú superior la acción que deseas realizar")
        label_info.pack()

        #Menu desplegable
        menu_admin = tk.Menu(frame)
        frame.config(menu=menu_admin)
        opcion_gestion_cuentas = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Cuentas", menu=opcion_gestion_cuentas)
        opcion_gestion_cuentas.add_command(label="Crear cuenta")
        opcion_gestion_cuentas.add_command(label="Ver cuenta")
        opcion_gestion_cuentas.add_command(label="Editar cuenta")
        opcion_gestion_maestros = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Maestros", menu=opcion_gestion_maestros)
        opcion_gestion_maestros.add_command(label="Crear Maestro", command=lambda: Crear_Maestro.crear_maestro(cuenta, frame))
        opcion_gestion_maestros.add_command(label="Ver Maestro", command=lambda: Ver_Maestro.ver_maestro(cuenta, frame))
        opcion_gestion_maestros.add_command(label="Editar Maestro")
        opcion_gestion_sedes = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Sedes", menu=opcion_gestion_sedes)
        opcion_gestion_sedes.add_command(label="Ver Sede")
        opcion_gestion_sedes.add_command(label="Editar Sede")


    @classmethod
    def menu_inicial_Clinico(cls, cuenta, frame):
        imprimir_titulo(frame, "Menu Inicial Clinico")
        frame_inicial = ttk.Frame()
        frame_inicial.pack(fill=tk.BOTH, expand=1)
        label_info = ttk.Label(frame_inicial, text="Bienvenido por favor selecciona en el menú superior la acción que deseas realizar")
        label_info.pack()

        #Menu desplegable
        menu_admin = tk.Menu(frame)
        frame.config(menu=menu_admin)
        opcion_gestion_cuentas = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Cuentas", menu=opcion_gestion_cuentas)
        opcion_gestion_cuentas.add_command(label="Ver cuenta")
        opcion_gestion_maestros = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Maestros", menu=opcion_gestion_maestros)
        opcion_gestion_maestros.add_command(label="Ver Maestro")
        opcion_gestion_sedes = tk.Menu(menu_admin, tearoff=0)
        menu_admin.add_cascade(label="Gestion Sedes", menu=opcion_gestion_sedes)
        opcion_gestion_sedes.add_command(label="Ver Sede")


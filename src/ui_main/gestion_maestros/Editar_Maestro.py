import tkinter as tk
from tkinter import ttk, messagebox

from src.base_datos.Gestor_Base import Gestor_Base
from src.ui_main.Cambiar_Estado import Cambiar_Estado
from src.ui_main.gestion_maestros.Crear_Maestro import Crear_Maestro
from src.ui_main.gestion_maestros.Editar_Categorias import Editar_Categorias
from src.ui_main.gestion_maestros.Editar_Datos_Basicos_Maestro import Editar_Datos_Basicos_Maestro
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
from src.ui_main.herramientas.interfaz_observacion import Interfaz_Observacion
from src.ui_main.herramientas.volver_menu import volver_menu
class Editar_Maestro:
    @classmethod
    def editar_maestro(cls, cuenta, ventana):
        def encontrar_maestro():
            busqueda = Gestor_Base.buscar_objeto(entrada_nombre.get(), "Maestro")
            if busqueda is None:
                from src.ui_main.Menu_inicial import Menu_inicial
                if "Administrativo" in cuenta.rol:
                    respuesta = messagebox.askyesno("Maestro no encontrado",
                                                    "No existe el maestro. ¿Desea registrar un maestro?")
                    if respuesta:
                        Crear_Maestro.crear_maestro(cuenta, ventana)
                    else:
                        Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)
                else:
                    messagebox.showerror("Error", "El maestro no existe.")
                    Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)
                return
            id, maestro = busqueda
            from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
            estado = "Habilitado" if maestro.estado else "Deshabilitado"
            imprimir_titulo(ventana, "Editar " + maestro.nombre + " Estado: " + estado)
            frame = ttk.Frame(ventana)
            frame.pack(pady=20)
            label_opcion = tk.Label(frame, text="Selecciona una opción: ")
            label_opcion.pack(pady=20)
            boton_datos = tk.Button(frame, text="Editar datos basicos", command=lambda: Editar_Datos_Basicos_Maestro.editar_datos_basicos(maestro, cuenta, id, ventana))
            boton_datos.pack(pady=20)
            boton_categorias = tk.Button(frame, text="Editar categorias", command=lambda: Editar_Categorias.modificar_categoria(maestro, cuenta, id, ventana))
            boton_categorias.pack(pady=20)
            if maestro.estado:
                boton_estado = tk.Button(frame, text="Deshabilitar", command=lambda: Interfaz_Observacion.generar_observacion(cuenta, maestro, id, ventana, "estado"))
                boton_estado.pack(pady=20)
            else:
                boton_estado = tk.Button(frame, text="Habilitar",
                                         command=lambda: Interfaz_Observacion.generar_observacion(cuenta, maestro, id,
                                                                                                  ventana, "estado"))
                boton_estado.pack(pady=20)
            boton_volver = tk.Button(frame, text="Cancelar", command=lambda: volver_menu(cuenta, ventana))
            boton_volver.pack(pady=20)
        from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
        imprimir_titulo(ventana, "Buscar maestro")
        frame = ttk.Frame(ventana)
        frame.pack()
        label_nombre = tk.Label(frame, text="Ingrese el nombre del maestro")
        label_nombre.pack(pady=5)
        entrada_nombre = tk.Entry(frame)
        entrada_nombre.pack(pady=5)
        boton_buscar = tk.Button(frame, text="Buscar maestro", command=encontrar_maestro)
        boton_buscar.pack()
        boton_volver = tk.Button(frame, text="Volver al menú inicial",
                                 command=lambda: volver_menu(cuenta, ventana))
        boton_volver.pack(pady=20)
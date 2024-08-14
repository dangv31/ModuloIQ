import tkinter as tk
from tkinter import messagebox

from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Categoria import Categoria
from src.gestor_aplicacion.Maestro import Maestro
from src.gestor_aplicacion.Observacion import Observacion
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo

class Interfaz_Observacion:
    @classmethod
    def generar_observacion(cls, cuenta, objeto, id, ventana, maestro):
        def registrar_observacion():
            detalle = entry_detalle.get()
            if isinstance(objeto, Categoria):
                objeto.maestro.observaciones.append(Observacion(cuenta, detalle))
                Gestor_Base.actualizar_objeto(objeto, id)
                from src.ui_main.gestion_maestros.Editar_Datos_Basicos_Maestro import Editar_Datos_Basicos_Maestro
                Editar_Datos_Basicos_Maestro.editar_datos_basicos(maestro, cuenta, id, ventana)

            else:
                objeto.observaciones.append(Observacion(cuenta, detalle))
                Gestor_Base.actualizar_objeto(objeto, id)
                if isinstance(objeto, Maestro):
                    from src.ui_main.gestion_maestros.Editar_Datos_Basicos_Maestro import Editar_Datos_Basicos_Maestro
                    Editar_Datos_Basicos_Maestro.editar_datos_basicos(maestro, cuenta, id, ventana)

            messagebox.showinfo("Éxito", "¡Observación registrada con éxito!")

        imprimir_titulo(ventana, "Generar observacion")

        label = tk.Label(ventana, text="Ingrese el motivo de los cambios:")
        label.pack(pady=10)

        entry_detalle = tk.Entry(ventana, width=50)
        entry_detalle.pack(pady=10)

        btn_registrar = tk.Button(ventana, text="Registrar Observación", command=registrar_observacion)
        btn_registrar.pack(pady=10)

import tkinter as tk
from tkinter import messagebox

from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Categoria import Categoria
from src.gestor_aplicacion.Maestro import Maestro
from src.gestor_aplicacion.Observacion import Observacion
from src.ui_main.herramientas.imprimir_titulo import imprimir_titulo
from src.ui_main.Cambiar_Estado import Cambiar_Estado

class Interfaz_Observacion:
    @classmethod
    def generar_observacion(cls, cuenta, objeto, id, ventana, tipo_cambio):
        def registrar_observacion():
            detalle = entry_detalle.get()
            if tipo_cambio == "info":
                objeto.observaciones.append(Observacion(cuenta, detalle))
                Gestor_Base.actualizar_objeto(objeto, id)

            elif tipo_cambio == "estado":
                Cambiar_Estado.cambiar_estado(objeto, cuenta, id)
                objeto.observaciones.append(Observacion(cuenta, detalle))
                Gestor_Base.actualizar_objeto(objeto, id)
            messagebox.showinfo("Éxito", "¡Observación y cambio registrado con éxito!")
            from src.ui_main.Menu_inicial import Menu_inicial
            Menu_inicial.menu_inicial_Administrativo(cuenta, ventana)
        imprimir_titulo(ventana, "Generar observacion")

        label = tk.Label(ventana, text="Ingrese el motivo de los cambios:")
        label.pack(pady=10)

        entry_detalle = tk.Entry(ventana, width=50)
        entry_detalle.pack(pady=10)

        btn_registrar = tk.Button(ventana, text="Registrar Observación", command=registrar_observacion)
        btn_registrar.pack(pady=10)

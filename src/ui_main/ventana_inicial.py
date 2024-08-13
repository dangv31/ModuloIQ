import tkinter as tk
from Inicio_sesion import Inicio_sesion

ventana = tk.Tk()
ventana.title("MedPlus - Sistema de gestion hospitalaria")
ventana.geometry("1280x720")

Inicio_sesion.inicio_sesion(ventana)

ventana.mainloop()
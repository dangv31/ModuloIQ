import tkinter as tk

def imprimir_titulo(frame,encabezado):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text=encabezado, bg="white", font=("Helvetica", 10, "bold"))
    titulo.pack()
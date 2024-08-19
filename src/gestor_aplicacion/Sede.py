class Sede:
    lista_sedes = []
    def __init__(self, nombre, quirofanos, salas_de_espera, consultorios,
                 direccion, pacientes, sillas, camas, ambulancias):
        self.nombre = nombre
        self.quirofanos = quirofanos
        self.salas_de_espera = salas_de_espera
        self.personal = []
        self.consultorios = consultorios
        self.direccion = direccion
        self.pacientes = pacientes
        self.sillas = sillas
        self.camas = camas
        self.ambulancias = ambulancias
        self.estado = True
        self.observaciones = []

    def imprimir_info(self):
        import tkinter as tk

        tk.Label(ventana, text="-------------Información de Sede-------------").pack()
        tk.Label(ventana, text="Nombre: " + self.nombre).pack()
        tk.Label(ventana, text="Quirófanos: " + str(self.quirofanos)).pack()
        tk.Label(ventana, text="Salas de espera: " + str(self.salas_de_espera)).pack()
        tk.Label(ventana, text="Personal: " + str(len(self.personal))).pack()
        tk.Label(ventana, text="Consultorios: " + str(self.consultorios)).pack()
        tk.Label(ventana, text="Dirección: " + self.direccion).pack()
        tk.Label(ventana, text="Pacientes: " + str(self.pacientes)).pack()
        tk.Label(ventana, text="Sillas: " + str(self.sillas)).pack()
        tk.Label(ventana, text="Camas: " + str(self.camas)).pack()
        tk.Label(ventana, text="Ambulancias: " + str(self.ambulancias)).pack()
        tk.Label(ventana, text="Estado: " + ("habilitada" if self.estado else "deshabilitada")).pack()
    def __str__(self):
        return self.nombre


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
        print("-------------Informacion de sede-------------")
        print("Nombre:", self.nombre)
        print("Quirofanos:", self.quirofanos)
        print("Salas de espera:", self.salas_de_espera)
        print("Personal:", len(self.personal))
        print("Consultorios:", self.consultorios)
        print("Direccion:", self.direccion)
        print("Pacientes:", self.pacientes)
        print("Sillas:", self.sillas)
        print("Camas:", self.camas)
        print("Ambulancias:", self.ambulancias)
        print("Estado: ", "habilitada" if self.estado else "deshabilitada")
    def __str__(self):
        return self.nombre


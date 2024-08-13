class Cuenta():
    lista_cuentas = []
    def __init__(self, nombres, apellidos, doc, nacimiento,  correo, contrasena):
        self.nombres = nombres
        self.apellidos = apellidos
        self.doc = doc
        self.nacimiento = nacimiento
        self.correo = correo
        self.contrasena = contrasena
        self.rol = []
        self.sede = []
        self.estado = True
        self.observaciones = []
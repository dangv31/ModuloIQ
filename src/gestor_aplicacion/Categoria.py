class Categoria():
    def __init__(self, info, maestro):
        self.info = info
        self.maestro = maestro
        self.estado = True
        self.maestro.categorias.append(self)
    def actualizar_info(self, informacion_nueva, indice):
        self.info[indice] = informacion_nueva

    def __str__(self):
        return f"{' '.join(self.info)} Estado: {self.estado}"

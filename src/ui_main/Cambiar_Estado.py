from src.base_datos.Gestor_Base import Gestor_Base
from src.gestor_aplicacion.Observacion import Observacion


class Cambiar_Estado:
    @classmethod
    def cambiar_estado(cls, objeto, cuenta, id):
        if objeto.estado:
            objeto.estado = False
        else:
            objeto.estado = True
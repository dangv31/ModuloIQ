import pickle
import sqlite3
import os

from src.gestor_aplicacion.Categoria import Categoria
from src.gestor_aplicacion.Cuenta import Cuenta
from src.gestor_aplicacion.Maestro import Maestro
from src.gestor_aplicacion.Sede import Sede


class Gestor_Base:
    @classmethod
    def guardar_objeto(cls, objeto):
        directorio = os.path.dirname(os.path.abspath(__file__))
        if isinstance(objeto, Maestro):
            ruta_base_datos = os.path.join(directorio, 'maestros.db')
            conn = sqlite3.connect(ruta_base_datos)
            c = conn.cursor()
            objeto = pickle.dumps(objeto)
            c.execute("INSERT INTO maestros (Maestro) VALUES (?)", (objeto,))
            conn.commit()
            conn.close()
            return
        elif isinstance(objeto, Sede):
            ruta_base_datos = os.path.join(directorio, 'sedes.db')
            conn = sqlite3.connect(ruta_base_datos)
            c = conn.cursor()
            objeto = pickle.dumps(objeto)
            c.execute("INSERT INTO sedes (Sede) VALUES (?)", (objeto,))
            conn.commit()
            conn.close()
            return
        elif isinstance(objeto, Cuenta):
            ruta_base_datos = os.path.join(directorio, 'cuentas.db')
            conn = sqlite3.connect(ruta_base_datos)
            c = conn.cursor()
            doc_cuenta = objeto.doc
            objeto = pickle.dumps(objeto)
            c.execute("INSERT INTO cuentas (ID, Cuenta) VALUES (?, ?)", (doc_cuenta, objeto))
            conn.commit()
            conn.close()
            return
    @classmethod
    def buscar_objeto(cls, busqueda, clase):
        directorio = os.path.dirname(os.path.abspath(__file__))
        if clase == "Maestro":
            ruta_base_datos = os.path.join(directorio, 'maestros.db')
            conn = sqlite3.connect(ruta_base_datos)
            c = conn.cursor()
            c.execute("SELECT * FROM maestros")
            lista_maestros = c.fetchall()
            for ID, maestro in lista_maestros:
                maestro = pickle.loads(maestro)
                if maestro.nombre == busqueda:
                    return ID, maestro
            return None
        elif clase == "Sede":
            ruta_base_datos = os.path.join(directorio, 'sedes.db')
            conn = sqlite3.connect(ruta_base_datos)
            c = conn.cursor()
            c.execute("SELECT * FROM sedes")
            lista_sedes = c.fetchall()
            for ID, sede in lista_sedes:
                sede = pickle.loads(sede)
                if sede.nombre == busqueda:
                    return ID, sede
            return None
        elif clase == "Cuenta":
            ruta_base_datos = os.path.join(directorio, 'cuentas.db')
            conn = sqlite3.connect(ruta_base_datos)
            c = conn.cursor()
            c.execute("SELECT * FROM cuentas")
            lista_cuentas = c.fetchall()
            for ID, cuenta in lista_cuentas:
                cuenta = pickle.loads(cuenta)
                if cuenta.doc == busqueda:
                    return ID, cuenta
            return None
    @classmethod
    def actualizar_objeto(cls, objeto, id):
        directorio = os.path.dirname(os.path.abspath(__file__))
        if isinstance(objeto, Maestro):
            ruta_base_datos = os.path.join(directorio, 'maestros.db')
            conn = sqlite3.connect(ruta_base_datos)
            c = conn.cursor()
            objeto = pickle.dumps(objeto)
            c.execute("UPDATE maestros SET Maestro = ? WHERE ID = ?", (objeto, id))
            conn.commit()
            conn.close()
        if isinstance(objeto, Sede):
            ruta_base_datos = os.path.join(directorio, 'sedes.db')
            conn = sqlite3.connect(ruta_base_datos)
            c = conn.cursor()
            objeto = pickle.dumps(objeto)
            c.execute("UPDATE sedes SET Sede = ? WHERE ID = ?", (objeto, id))
            conn.commit()
            conn.close()
        if isinstance(objeto, Cuenta):
            ruta_base_datos = os.path.join(directorio, 'cuentas.db')
            conn = sqlite3.connect(ruta_base_datos)
            c = conn.cursor()
            objeto = pickle.dumps(objeto)
            c.execute("UPDATE cuentas SET Cuenta = ? WHERE ID = ?", (objeto, id))
            conn.commit()
            conn.close()
    @classmethod
    def lista_maestros(cls):
        directorio = os.path.dirname(os.path.abspath(__file__))
        ruta_base_datos = os.path.join(directorio, 'maestros.db')
        conn = sqlite3.connect(ruta_base_datos)
        c = conn.cursor()
        c.execute("SELECT * FROM maestros")
        lista_maestros = c.fetchall()
        maestros_deserializados = []
        for ID, maestro in lista_maestros:
            maestros_deserializados.append((ID, pickle.loads(maestro)))
        return maestros_deserializados
    @classmethod
    def lista_cuentas(cls):
        directorio = os.path.dirname(os.path.abspath(__file__))
        ruta_base_datos = os.path.join(directorio, 'cuentas.db')
        conn = sqlite3.connect(ruta_base_datos)
        c = conn.cursor()
        c.execute("SELECT * FROM cuentas")
        lista_cuentas = c.fetchall()
        cuentas_deserializados = []
        for ID, cuenta in lista_cuentas:
            cuentas_deserializados.append((ID, pickle.loads(cuenta)))
        return cuentas_deserializados

    @classmethod
    def lista_sedes(cls):
        directorio = os.path.dirname(os.path.abspath(__file__))
        ruta_base_datos = os.path.join(directorio, 'sedes.db')
        conn = sqlite3.connect(ruta_base_datos)
        c = conn.cursor()
        c.execute("SELECT * FROM sedes")
        lista_sedes = c.fetchall()
        sedes_deserializados = []
        for ID, sede in lista_sedes:
            sedes_deserializados.append((ID, pickle.loads(sede)))
        return sedes_deserializados

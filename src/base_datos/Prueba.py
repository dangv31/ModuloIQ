import pickle
import sqlite3
import os

directorio = os.path.dirname(os.path.abspath(__file__))
ruta_base_datos = os.path.join(directorio, 'maestros.db')
conn = sqlite3.connect(ruta_base_datos)

c = conn.cursor()
#Crear tabla
#c.execute("""CREATE TABLE estudiantes(
#                ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                Sede TEXT
#)""")
#Agregar un dato a la tabla
#c.execute("INSERT INTO estudiantes VALUES ('mark', 27, 1.90)")
#todos_estudiantes = [
#    ('Juan', 30, 1.80),
#    ('Pepe', 20, 1.60),
#    ('Messi', 80, 1.70),
#    ('Cr7', 40, 1.90)
#]
#Agregar varios datos a la tabla
#c.executemany("INSERT INTO estudiantes VALUES (?, ?, ?)", todos_estudiantes)
#Abrir los datos de la tabla
c.execute("SELECT * FROM maestros")
lista = c.fetchall()
for ID, maestro in lista:
    print(ID, pickle.loads(maestro))
conn.commit()
conn.close()


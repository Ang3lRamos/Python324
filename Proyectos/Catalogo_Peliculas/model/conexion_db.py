import sqlite3

class ConexionDB:
    def __init__(self):
        #abre la conexion
        self.base_datos = "database/peliculas.db"#lo busca si no lo encuentra la crea
        self.conexion = sqlite3.connect(self.base_datos)#hace la conexion con la base de datos
        self.cursor = self.conexion.cursor()#sirve para ejecutar un sql dentro de la base de datos
        
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()#cierra la conexion
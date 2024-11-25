# modelo_usuarios.py
import sqlite3


class ModeloUsuarios:
    def __init__(self, db_path="src\model\database\heroesdelbalon.db"):
        self.db_path = db_path

    def obtener_usuarios(self):
        """Devuelve una lista de todos los usuarios activos (baja_usuario = 0)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_usuario, nombre_usuario, admin, score FROM usuario WHERE baja_usuario = 0"
        )
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios

    def insertar_usuario(self, nombre_usuario, password, admin, score):
        """Inserta un nuevo usuario en la tabla usuario."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuario (nombre_usuario, password, admin, baja_usuario, score) VALUES (?, ?, ?, 0, ?)",
            (nombre_usuario, password, admin, score),
        )
        conn.commit()
        conn.close()

    def actualizar_usuario(self, id_usuario, nombre_usuario, password, admin, score):
        """Actualiza un usuario existente."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE usuario SET nombre_usuario = ?, password = ?, admin = ?, score = ? WHERE id_usuario = ?",
            (nombre_usuario, password, admin, score, id_usuario),
        )
        conn.commit()
        conn.close()

    def eliminar_usuario(self, id_usuario):
        """Marca un usuario como dado de baja (baja_usuario = 1)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE usuario SET baja_usuario = 1 WHERE id_usuario = ?", (id_usuario,)
        )
        conn.commit()
        conn.close()

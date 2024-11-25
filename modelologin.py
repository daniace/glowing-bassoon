import sqlite3


class ModeloLogin:
    def __init__(self, db_path="src\model\database\heroesdelbalon.db"):
        self.db_path = db_path

    def validar_usuario(self, username, password):
        """Valida si las credenciales son correctas."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM usuario WHERE nombre_usuario = ? AND password = ? AND admin = 1",
            (username, password),
        )
        user = cursor.fetchone()
        conn.close()
        return user is not None

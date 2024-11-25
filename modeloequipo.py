# modelo_equipos.py
import sqlite3


class ModeloEquipo:
    def __init__(self, db_path="src\model\database\heroesdelbalon.db"):
        self.db_path = db_path

    def obtener_equipos(self):
        """Devuelve una lista de todos los equipos activos (baja_equipo = 0)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_equipo, id_usuario, nombre_equipo, id_carta1, id_carta2, id_carta3, id_carta4, id_carta5, id_carta6, id_carta7, id_carta8, id_carta9, id_carta10, id_carta11 FROM equipo WHERE baja_equipo = 0"
        )
        equipos = cursor.fetchall()
        conn.close()
        return equipos

    def insertar_equipo(
        self,
        nombre_equipo,
        carta1,
        carta2,
        carta3,
        carta4,
        carta5,
        carta6,
        carta7,
        carta8,
        carta9,
        carta10,
        carta11,
    ):
        """Inserta un nuevo equipo en la tabla equipo."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO equipo (nombre_equipo, carta1, carta2, carta3, carta4, carta5, carta6, carta7, carta8, carta9, carta10, carta11, baja_equipo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)",
            (
                nombre_equipo,
                carta1,
                carta2,
                carta3,
                carta4,
                carta5,
                carta6,
                carta7,
                carta8,
                carta9,
                carta10,
                carta11,
            ),
        )
        conn.commit()
        conn.close()

    def actualizar_equipo(
        self,
        id_equipo,
        id_usuario,
        nombre_equipo,
        carta1,
        carta2,
        carta3,
        carta4,
        carta5,
        carta6,
        carta7,
        carta8,
        carta9,
        carta10,
        carta11,
    ):
        """Actualiza un equipo existente."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE equipo SET id_usuario = ?, nombre_equipo = ?, carta1 = ?, carta2 = ?, carta3 = ?, carta4 = ?, carta5 = ?, carta6 = ?, carta7 = ?, carta8 = ?, carta9 = ?, carta10 = ?, carta11 = ? WHERE id_equipo = ?",
            (
                id_usuario,
                nombre_equipo,
                carta1,
                carta2,
                carta3,
                carta4,
                carta5,
                carta6,
                carta7,
                carta8,
                carta9,
                carta10,
                carta11,
                id_equipo,
            ),
        )
        conn.commit()
        conn.close()

    def eliminar_equipo(self, id_equipo):
        """Marca un equipo como dado de baja (baja_equipo = 1)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE equipo SET baja_equipo = 1 WHERE id_equipo = ?", (id_equipo,)
        )
        conn.commit()
        conn.close()

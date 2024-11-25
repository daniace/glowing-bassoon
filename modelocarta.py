# modelo_cartas.py
import sqlite3


class ModeloCartas:
    def __init__(self, db_path="src\model\database\heroesdelbalon.db"):
        self.db_path = db_path

    def obtener_cartas(self):
        """Devuelve todas las cartas activas (deshabilitado = 0)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """SELECT id_carta, short_name, nationality, club_name, overall, player_positions, 
                pace, shooting, passing, dribbling, defending, physic, gk_diving,
                gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning
                FROM carta 
                WHERE deshabilitado = 0"""
        )
        cartas = cursor.fetchall()
        conn.close()
        return cartas

    def insertar_carta(
        self,
        short_name,
        nationality,
        club_name,
        overall,
        player_positions,
        pace,
        shooting,
        passing,
        dribbling,
        defending,
        physic,
    ):
        """Inserta una nueva carta en la tabla."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO carta 
                (short_name, nationality, club_name, overall, player_positions,
                pace, shooting, passing, dribbling, defending, physic, deshabilitado) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)""",
            (
                short_name,
                nationality,
                club_name,
                overall,
                player_positions,
                pace,
                shooting,
                passing,
                dribbling,
                defending,
                physic,
            ),
        )
        conn.commit()
        conn.close()

    def insertar_arquero(
        self,
        short_name,
        nationality,
        club_name,
        overall,
        gk_diving,
        gk_handling,
        gk_kicking,
        gk_reflexes,
        gk_speed,
        gk_positioning,
    ):
        """Inserta una nueva carta en la tabla."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO carta 
                (short_name, nationality, club_name, overall, player_positions,
                gk_diving, gk_handling, gk_kicking, gk_reflexes, gk_speed, gk_positioning, deshabilitado) 
                VALUES (?, ?, ?, ?, 'GK', ?, ?, ?, ?, ?, ?, 0)""",
            (
                short_name,
                nationality,
                club_name,
                overall,
                gk_diving,
                gk_handling,
                gk_kicking,
                gk_reflexes,
                gk_speed,
                gk_positioning,
            ),
        )
        conn.commit()
        conn.close()

    def actualizar_carta(
        self,
        id_carta,
        short_name,
        nationality,
        club_name,
        overall,
        player_positions,
        pace,
        shooting,
        passing,
        dribbling,
        defending,
        physic,
    ):
        """Actualiza los datos de una carta."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE carta 
                SET short_name = ?, nationality = ?, club_name = ?, overall = ?,
                player_positions = ?, pace = ?, shooting = ?, passing = ?, 
                dribbling = ?, defending = ?, physic = ? 
                WHERE id_carta = ?""",
            (
                short_name,
                nationality,
                club_name,
                overall,
                player_positions,
                pace,
                shooting,
                passing,
                dribbling,
                defending,
                physic,
                id_carta,
            ),
        )
        conn.commit()
        conn.close()

    def actualizar_arquero(
        self,
        id_carta,
        short_name,
        nationality,
        club_name,
        overall,
        gk_diving,
        gk_handling,
        gk_kicking,
        gk_reflexes,
        gk_speed,
        gk_positioning,
    ):
        """Actualiza los datos de una carta."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE carta 
                SET short_name = ?, nationality = ?, club_name = ?, overall = ?, 
                gk_diving = ?, gk_handling = ?, gk_kicking = ?, 
                gk_reflexes = ?, gk_speed = ?, gk_positioning = ? 
                WHERE id_carta = ?""",
            (
                short_name,
                nationality,
                club_name,
                overall,
                gk_diving,
                gk_handling,
                gk_kicking,
                gk_reflexes,
                gk_speed,
                gk_positioning,
                id_carta,
            ),
        )
        conn.commit()
        conn.close()

    def eliminar_carta(self, id_carta):
        """Marca una carta como deshabilitada (deshabilitado = 1)."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE carta SET deshabilitado = 1 WHERE id_carta = ?", (id_carta,)
        )
        conn.commit()
        conn.close()

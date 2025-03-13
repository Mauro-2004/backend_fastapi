import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.atributoxusuario_model import Atributoxusuario
from fastapi.encoders import jsonable_encoder



class AtributoxusuarioController:

    def create_atributoxusuario(self, atributoxusuario: Atributoxusuario):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO atributoxusuario (id_usuario, id_atriduto, estado) VALUES (%s, %s, %s)",
                (atributoxusuario.id_usuario, atributoxusuario.id_atriduto, atributoxusuario.estado)
            )
            conn.commit()
            return {"mensaje": "Atributoxusuario creado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_atributoxusuario(self, atributoxusuario_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributoxusuario WHERE id = %s", (atributoxusuario_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id': result[0],
                    'id_usuario': result[1],
                    'id_atriduto': result[2],
                    'estado': result[3]
               }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Atributoxusuario no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_atributoxusuarios(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributoxusuario")
            result = cursor.fetchall()
            payload = []

            for data in result:
                content = {
                    'id': data[0],
                    'id_usuario': data[1],
                    'id_atriduto': data[2],
                    'estado': data[3]
                }
                payload.append(content)

            return {"resultado": jsonable_encoder(payload)}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_atributoxusuario(self, atributoxusuario_id: int, atributoxusuario: Atributoxusuario):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE atributoxusuario SET id_usuario = %s, id_atriduto = %s, estado = %s WHERE id = %s",
                (atributoxusuario.id_usuario, atributoxusuario.id_atriduto, atributoxusuario.estado, atributoxusuario_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributoxusuario no encontrado")
            return {"mensaje": "Atributoxusuario actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_atributoxusuario(self, atributoxusuario_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM atributoxusuario WHERE id = %s", (atributoxusuario_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributoxusuario no encontrado")
            return {"mensaje": "Atributoxusuario eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

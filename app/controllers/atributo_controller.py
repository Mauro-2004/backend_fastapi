import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.atributo_model import Atributo
from fastapi.encoders import jsonable_encoder

class AtributoController:

    def create_atributo(self, atributo: Atributo):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO atributo (nombre, descripcion) VALUES (%s, %s)",
                (atributo.nombre, atributo.descripcion)
            )
            conn.commit()
            return {"mensaje": "Atributo creado exitosamente"}
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_atributo(self, atributo_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo WHERE id = %s", (atributo_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id': result[0],
                    'nombre': result[1],
                    'descripcion': result[2]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Atributo no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_atributos(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo")
            result = cursor.fetchall()
            payload = []

            for data in result:
                content = {
                    'id': data[0],
                    'nombre': data[1],
                    'descripcion': data[2]
                }
                payload.append(content)

            return {"resultado": jsonable_encoder(payload)}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_atributo(self, atributo_id: int, atributo: Atributo):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE atributo SET nombre = %s, descripcion = %s WHERE id = %s",
                (atributo.nombre, atributo.descripcion, atributo_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributo no encontrado")
            return {"mensaje": "Atributo actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_atributo(self, atributo_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM atributo WHERE id = %s", (atributo_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributo no encontrado")
            return {"mensaje": "Atributo eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

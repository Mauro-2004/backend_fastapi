import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.rol_model import Rol
from fastapi.encoders import jsonable_encoder

class RolController:

    def create_perfil(self, rol: Rol):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO rol (nombre, descripcion,estado) VALUES (%s, %s,%s)",
                (rol.nombre, rol.descripcion, rol.estado)
            )
            conn.commit()
            return {"mensaje": "rol creado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def get_rol(self, rol_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM rol WHERE id = %s", (rol_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="rol not found")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def get_roles(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM rol")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def delete_rol(self, rol_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(" UPDATE rol SET estado = 0  WHERE id = %s", (rol_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="rol not found")
            return {"mensaje": "rol eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def update_rol(self, rol_id: int, rol: Rol):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE rol SET nombre = %s, descripcion , %s estado = %s WHERE id = %s",
                (rol.nombre, rol.descripcion, rol.estado, rol_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="rol no encontrado o no se realizaron cambios")
            return {"mensaje": "rol actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()
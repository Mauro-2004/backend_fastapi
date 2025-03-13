import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.productos_model import Productos

class ProductosController:

    def create_productos(self, productos: Productos):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO productos (nombre, descripcion, estado_alquiler, estado, fecha_creacion) VALUES (%s, %s, %s, %s, %s)",
                (productos.nombre, productos.descripcion, productos.estado_alquiler, productos.estado, productos.fecha_de_creacion)
            )
            conn.commit()
            return {"mensaje": "Producto creado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def get_productos(self, productos_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos WHERE id_productos = %s", (productos_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Producto no encontrado")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()



    def get_productos(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def delete_productos(self, productos_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE productos SET estado = 0 WHERE id_herramienta = %s", (productos_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Producto no encontrado")
            return {"mensaje": "Producto eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()


    def update_productos(self, productos_id: int, productos: Productos):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE productos SET nombre = %s, descripcion = %s, estado_alquiler = %s, estado = %s,%s fecha_creacion, WHERE id_herramienta = %s ",
                (productos.nombre, productos.descripcion, productos.estado_alquiler, productos.estado,productos.fecha_creacion, productos_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Producto no encontrado o no se realizaron cambios")
            return {"mensaje": "Producto actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()


def get_herramienta_controller():
        return ProductosController()


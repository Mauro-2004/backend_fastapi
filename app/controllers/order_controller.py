import mysql.connector
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.order_model import Order
from fastapi.encoders import jsonable_encoder

class OrderController:

    def create_order(self, order: Order):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO order (user_id, user_nombre ,estado, total) VALUES (%s, %s, %s, %s)",
                (order.user_id, order.user_nombre ,order.estado, order.total)
            )
            conn.commit()
            return {"mensaje": "Orden creada exitosamente"}
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_order(self, order_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM order WHERE id_order = %s", (order_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id': result[0],
                    'user_nombre': result[1],
                    'estado': result[2]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Orden no encontrada")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_orders(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM order")
            result = cursor.fetchall()
            payload = []

            for data in result:
                content = {
                    'id': data[0],
                    'user_nombre': data[1],
                    'estado': data[2]
                }
                payload.append(content)

            return {"resultado": jsonable_encoder(payload)}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_order(self, order_id: int, order: Order):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE order SET user_nombre = %s, estado = %s WHERE id_order = %s",
                (order.nombre, order.estado, order_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Orden no encontrada o no se realizaron cambios")
            return {"mensaje": "Orden actualizada exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_order(self, order_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE order SET estado = 0 WHERE id_order = %s", (order_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Orden no encontrada")
            return {"mensaje": "Estado de la orden actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

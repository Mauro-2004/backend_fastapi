from mysql.connector import Error as MySQLError
from fastapi import HTTPException
from app.config.db_config import get_db_connection
from app.models.user_model import User, Login
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta
import jwt

SECRET_KEY = "fsdfsdfsdfsdfs"
class UserController:

    def create_user(self, user: User):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO usuario (nombre, apellido, documento, telefono, email ,password ,id_rol, id_producto, estado)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                        (user.nombre, user.apellido ,user.documento, user.telefono,  user.email ,user.password, user.id_rol, user.producto ,user.estado)
                    )
                    conn.commit()
            return {"mensaje": "Usuario creado exitosamente"}
        except MySQLError as err:
            raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {str(err)}")

    def get_user(self, user_id: int):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM usuario WHERE id = %s AND estado = 1", (user_id,))
                    result = cursor.fetchone()
                    if result:
                        content = {
                            'id': result[0],
                            'nombre': result[1],
                            'apellido': result[2],
                            'documento': result[3],
                            'telefono': result[4],
                            'email': result[5],
                            'password': result[6],
                            'id_rol': result[7],
                            'id_producto': result[8],
                            'estado': result[9]
                        }
                        return jsonable_encoder(content)
                    else:
                        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        except MySQLError as err:
            raise HTTPException(status_code=500, detail=f"Error al obtener el usuario: {str(err)}")

    def get_users(self):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM usuario WHERE estado = 1")
                    result = cursor.fetchall()
                    payload = [
                        {
                            'id': result[0],
                            'nombre': result[1],
                            'apellido': result[2],
                            'documento': result[3],
                            'telefono': result[4],
                            'email': result[5],
                            'password': result[6],
                            'id_rol': result[7],
                            'id_producto': result[8],
                            'estado': result[9]
                        }
                        for data in result
                    ]
                    return {"resultado": jsonable_encoder(payload)}
        except MySQLError as err:
            raise HTTPException(status_code=500, detail=f"Error al obtener los usuarios: {str(err)}")

    def create_access_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
            to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
        return encoded_jwt
    
    def login(self, user: Login):
            try:
                with get_db_connection() as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(
                            "SELECT id, email, id_rol FROM usuario WHERE nombre = %s AND password = %s AND estado = 1",
                            (user.usuario, user.contrasena)
                        )
                        result = cursor.fetchone()
                        if result:
                            content = {
                                'id': result[0],
                                'email': result[1],
                                'id_rol': result[2],
                            }
                            return {"resultado": [jsonable_encoder(content)]}
                        else:
                            raise HTTPException(status_code=404, detail="Usuario no encontrado")
            except MySQLError as err:
                raise HTTPException(status_code=500, detail=f"Error en el inicio de sesión: {str(err)}")
        



    def delete_user(self, user_id: int):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE usuario SET estado=%s WHERE id=%s
                        """, (user_id))
                    conn.commit()
                    if cursor.rowcount == 0:
                        raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return {"mensaje": "Usuario eliminado exitosamente"}
        except MySQLError as err:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {str(err)}")



        

    def update_user(self, user_id: int, user: User):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """UPDATE usuario SET nombre = %s, apellido = %s, documento = %s,
                            telefono = %s, email = %s ,password = %s, id_rol = %s, id_producto = %s, estado = %s WHERE id = %s AND estado = 1""",
                        (user.nombre, user.apellido, user.documento, user.telefono, user.email ,user.password ,user.telefono, user.id_rol, user.id_producto, user.estado, user_id)
                    )
                    conn.commit()
                    if cursor.rowcount == 0:
                        raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return {"mensaje": "Usuario actualizado exitosamente"}
        except MySQLError as err:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {str(err)}")


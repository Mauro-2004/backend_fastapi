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
                        """INSERT INTO usuarios (nombre, email, telefono, direccion, tipo_usuario, contraseña ,id_rol)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                        (user.nombre, user.email, user.telefono, user.direccion, user.tipo_usuario ,user.contraseña, user.id_rol)
                    )
                    conn.commit()
            return {"mensaje": "Usuario creado exitosamente"}
        except MySQLError as err:
            raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {str(err)}")

    def get_user(self, user_id: int):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s AND estado = 1", (user_id,))
                    result = cursor.fetchone()
                    if result:
                        content = {
                            'id_usuario': result[0],
                            'nombre': result[1],
                            'email': result[2],
                            'telefono': result[3],
                            'direccion': result[4],
                            'tipo_usuario': result[5],
                            'contraseña': result[6],
                            'id_rol': result[7]
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
                            'id_usuario': result[0],
                            'nombre': result[1],
                            'email': result[2],
                            'telefono': result[3],
                            'direccion': result[4],
                            'tipo_usuario': result[5],
                            'contraseña': result[6],
                            'id_rol': result[7]
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
                            "SELECT id_usuario, email, id_rol FROM usuarios WHERE nombre = %s AND contraseña = %s AND estado = 1",
                            (user.usuario, user.contrasena)
                        )
                        result = cursor.fetchone()
                        if result:
                            content = {
                                'id_usuario': result[0],
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
                        UPDATE usuarios SET estado=%s WHERE id_usuario=%s
                        """, (user_id))
                    conn.commit()
                    if cursor.rowcount == 0:
                        raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return {"mensaje": "Usuario eliminado exitosamente"}
        except MySQLError as err:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {str(err)}")



        

    def update_user(self: int, user: User):
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """UPDATE usuarios SET nombre = %s, email = %s,
                            telefono = %s, direccion = %s ,tipo_usuario = %s, contraseña = %s, id_rol = %s WHERE id_usuario = %s AND estado = 1""",
                        (user.nombre, user.email, user.telefono, user.direccion, user.tipo_usuario ,user.contraseña, user.id_rol)
                    )
                    conn.commit()
                    if cursor.rowcount == 0:
                        raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return {"mensaje": "Usuario actualizado exitosamente"}
        except MySQLError as err:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el usuario: {str(err)}")


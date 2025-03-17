from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.user_routes import router as user_router
from app.routes.rol_routes import router as rol_router
from app.routes.productos_routes import router as productos_router 
from app.routes.atributo_routes import router as atributo_router
from app.routes.atributoxusuario_routes import router as atributoxusuario_router
from app.routes.order_routes import router as order_router

app = FastAPI()

# Agrega el origen exacto de tu frontend
origins = [
    "http://localhost:5173",  # Asegúrate de incluir este puerto
    "https://backend-fastapi-gvnr.onrender.com","https://frontend-svelte-2.onrender.com"  # También puedes mantener este
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (POST, GET, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Incluir todos los routers
app.include_router(user_router)
app.include_router(rol_router)
app.include_router(productos_router)
app.include_router(atributo_router)
app.include_router(atributoxusuario_router)
app.include_router(order_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

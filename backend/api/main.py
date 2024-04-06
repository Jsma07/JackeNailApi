


from fastapi import FastAPI
from Routes.Usuarios.usuarioRoutes import router as usuariosRoutes
from Routes.Configuracion.RolRoutes import router as RolRoutes
from Routes.Configuracion.PermisoRoutes import router as PermisoRoutes

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Git hubbb!"}

app.include_router(usuariosRoutes)
app.include_router(RolRoutes)
app.include_router(PermisoRoutes)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


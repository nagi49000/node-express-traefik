from fastapi import FastAPI


def create_app():
    app = FastAPI(title="simple hola app")

    # adding in the root path here since traefik is cack at routing
    @app.get("/api-hola/hola")
    async def hola():
        return {"message": "Hola"}

    @app.get("/api-hola/sub-path/adios")
    async def adios():
        return {"message": "Adios"}

    return app


app = create_app()

from fastapi import FastAPI


def create_app():
    app = FastAPI(title="simple hola app")

    # adding in the root path here since traefik is cack at routing
    @app.get("/api-hola/hola")
    async def hello_world():
        return {"message": "Hola"}

    return app


app = create_app()

from fastapi import FastAPI


def create_app():
    app = FastAPI(title="simple hello app")

    @app.get("/hola")
    async def hello_world():
        return {"message": "Hola"}

    return app


app = create_app()

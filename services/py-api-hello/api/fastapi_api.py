from fastapi import FastAPI


def create_app():
    app = FastAPI(title="simple hello app")

    @app.get("/hello")
    async def hello_world():
        return {"message": "Hello"}

    return app


app = create_app()

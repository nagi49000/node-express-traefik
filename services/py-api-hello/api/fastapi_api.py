from fastapi import FastAPI


def create_app():
    app = FastAPI(title="simple hello app")

    # adding in the root path here since traefik is cack at routing
    @app.get("/api-hello/hello")
    async def hello_world():
        return {"message": "Hello"}

    return app


app = create_app()

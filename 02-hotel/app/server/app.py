from fastapi import FastAPI

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="PDP's Hotel",
        description="This is PDP's hotel",
        version="0.1",
    )
    return app_

from fastapi import FastAPI
from app.controllers import auth_controller,health_controller

app = FastAPI(
    title='Fluency Fusion Authentication',
    description='Fluency Fusion Authentication feature'
    )

app.include_router(auth_controller.router)
app.include_router(health_controller.router)

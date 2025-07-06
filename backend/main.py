from fastapi import FastAPI
from routers import user, code_confirmation

app = FastAPI()

app.include_router(user.router, tags=['user'])
app.include_router(code_confirmation.router, tags=['code_confirmation'])




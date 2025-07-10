from fastapi import FastAPI
from routers import user, code_confirmation, chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router, tags=['user'])
app.include_router(code_confirmation.router, tags=['code_confirmation'])
app.include_router(chat.router, tags=['chat'])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],          # Все методы: GET, POST, PUT и т.д.
    allow_headers=["*"],          # Все заголовки
)



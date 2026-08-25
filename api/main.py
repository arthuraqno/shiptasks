from fastapi import FastAPI
from routes.usuario import router as usuario_router
from routes.todo import router as todo_router

app = FastAPI()
app.include_router(usuario_router)
app.include_router(todo_router)

@app.get("/")
def home():
    return {"mensagem": "API shiptasks funcionando!"}


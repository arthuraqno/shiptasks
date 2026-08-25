from fastapi import APIRouter, Depends
from services.todo_service import TodoService
from schemas.todo import TodoCreate, TodoResponse
from auth import obter_usuario_atual

router = APIRouter()

todo_service = TodoService()

@router.get("/todos", response_model=list[TodoResponse])
def listar_todos():
    return todo_service.listar_todos()

@router.post("/todos", response_model=TodoResponse)
def cadastrar_todo(dados: TodoCreate, usuario=Depends(obter_usuario_atual)):
    return todo_service.cadastrar_todo(dados.titulo)

@router.put("/todos/{todo_id}/feito", response_model=TodoResponse)
def marcar_como_feito(todo_id: str, usuario=Depends(obter_usuario_atual)):
    return todo_service.marcar_como_feito(todo_id)

@router.delete("/todos/{todo_id}")
def deletar_todo(todo_id: str, usuario=Depends(obter_usuario_atual)):
    todo_service.deletar_todo(todo_id)
    return {"mensagem": "Tarefa deletada com sucesso!"}
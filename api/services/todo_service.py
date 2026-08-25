from database import db
from models.todo import Todo
from bson import ObjectId
from schemas.todo import TodoResponse

class TodoService:
    def cadastrar_todo(self, titulo: str):
        todo = Todo(titulo=titulo)
        resultado = db.todos.insert_one(todo.to_dict())
        
        todo_criado = db.todos.find_one({"_id": resultado.inserted_id})
        return self._to_response(todo_criado)

    def _to_response(self, todo_doc: dict) -> TodoResponse:
        return TodoResponse(
            id=str(todo_doc["_id"]),
            titulo=todo_doc["titulo"],
            feito=todo_doc["feito"],
            criado_em=todo_doc["criado_em"]
        )

    def listar_todos(self):
        todos = db.todos.find()
        return [self._to_response(todo) for todo in todos]  

    def marcar_como_feito(self, todo_id: str):
        db.todos.update_one(
            {"_id": ObjectId(todo_id)},
            {"$set": {"feito": True}}
        )
        todo_atualizado = db.todos.find_one({"_id": ObjectId(todo_id)})
        return self._to_response(todo_atualizado)

    def deletar_todo(self, todo_id: str):
        db.todos.delete_one(
            {"_id": ObjectId(todo_id)}
        )
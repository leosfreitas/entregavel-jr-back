from repositories.despesas_repository import DespesaRepository
from fastapi import Request, Response, HTTPException
import os
import jwt

class DeleteDespesaUseCase:
    def __init__(self, despesas_repository: DespesaRepository):
        self.despesas_repository = despesas_repository

    def execute(self, despesa_id: str, response: Response, request: Request):
        token = request.cookies.get("appraiser_auth_token")
        if not token:
            raise HTTPException(status_code=401, detail="Invalid token")

        payload = jwt.decode(
            token.split(" ")[1],
            os.getenv("APPRAISER_JWT_SECRET"),
            algorithms=["HS256"]
        )
        user_id = payload.get("id")
        if not user_id:
            response.status_code = 404
            return {"status": "error", "message": "Usuário não encontrado"}

        deleted = self.despesas_repository.delete_despesa_by_id(despesa_id, user_id)

        if not deleted:  
            response.status_code = 404
            return {"status": "error", "message": "Despesa não encontrada ou não pertence a este usuário"}

        response.status_code = 200
        return {"status": "success", "message": "Despesa deletada com sucesso"}

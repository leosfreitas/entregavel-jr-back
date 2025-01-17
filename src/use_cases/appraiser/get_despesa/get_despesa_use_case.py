from repositories.despesas_repository import DespesaRepository
from fastapi import Request, Response
from entities.despesa import Despesa
from fastapi import HTTPException
import os
import jwt

class GetDespesaUseCase:
    def __init__(self, despesas_repository: DespesaRepository):
        self.despesas_repository = despesas_repository

    def execute(self, despesa_id: str, response: Response, request: Request):
        despesa = self.despesas_repository.get_despesa_by_id(despesa_id)
        if not despesa:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 400
        return despesa
    
class GetDespesasUseCase:
    def __init__(self, despesas_repository: DespesaRepository):
        self.despesas_repository = despesas_repository

    def execute(self, response: Response, request: Request):
        token = request.cookies.get("appraiser_auth_token")
        if not token:
            raise HTTPException(status_code=401, detail="Invalid token")

        payload = jwt.decode(token.split(" ")[1], os.getenv("APPRAISER_JWT_SECRET"), algorithms=["HS256"])

        user_id = payload.get("id")
        appraiser_email = payload.get("email")
        request.state.auth_payload = {"appraiser_id": user_id, "appraiser_email": appraiser_email}

        if not user_id:
            response.status_code = 404
            return {"status": "error", "message":"Usuário não encontrado"}

        despesas = self.despesas_repository.get_despesa_by_user_id(user_id)
        if not despesas:
            response.status_code = 404
            return {"status": "error", "message": "Nenhuma despesa encontrada para o usuário"}

        response.status_code = 200
        return despesas

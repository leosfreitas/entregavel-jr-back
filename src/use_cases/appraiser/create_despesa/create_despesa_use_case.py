from use_cases.appraiser.create_despesa.create_despesa_dto import CreateDespesaDTO
from fastapi import Request, Response, HTTPException
from repositories.despesas_repository import DespesaRepository
from entities.despesa import Despesa
import jwt
import os

class CreateDespesaUseCase:
    def __init__(self, despesa_repository: DespesaRepository):
        self.despesa_repository = despesa_repository

    def execute(self, create_despesa_dto: CreateDespesaDTO, response: Response, request: Request):
        token = request.cookies.get("appraiser_auth_token")
        if not token:
            raise HTTPException(status_code=401, detail="Invalid token")

        payload = jwt.decode(token.split(" ")[1], os.getenv("APPRAISER_JWT_SECRET"), algorithms=["HS256"])

        user_id = payload.get("id")
        appraiser_email = payload.get("email")
        request.state.auth_payload = {"appraiser_id": user_id, "appraiser_email": appraiser_email}

        if not user_id:
            response.status_code = 407
            return {"status": "error", "message":"Usuário não encontrado"}

        despesa = Despesa(
            user=user_id,
            tipo=create_despesa_dto.tipo,
            valor=create_despesa_dto.valor,
            data=create_despesa_dto.data,
            descricao=create_despesa_dto.descricao
        )

        self.despesa_repository.save(despesa)
        response.status_code=200
        return {"status": "success", "message":"Despesa criada"}

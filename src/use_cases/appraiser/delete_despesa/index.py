from repositories.despesas_repository import DespesaRepository
from .delete_despesa_use_case import DeleteDespesaUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

delete_despesa_use_case = DeleteDespesaUseCase(DespesaRepository())

@router.delete("/user/delete-despesa/{despesa_id}")
def delete_despesa(despesa_id: str, response: Response, request: Request):
    return delete_despesa_use_case.execute(despesa_id, response, request)
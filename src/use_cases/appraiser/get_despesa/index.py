from repositories.despesas_repository import DespesaRepository
from .get_despesa_use_case import GetDespesaUseCase, GetDespesasUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

get_despesa_use_case = GetDespesaUseCase(DespesaRepository())
get_despesas_use_case = GetDespesasUseCase(DespesaRepository())

@router.get("/user/get-despesa/{despesa_id}")
def get_despesa(despesa_id: str ,response:Response, request:Request):
    return get_despesa_use_case.execute(despesa_id,response, request)

@router.get("/user/get-despesas")
def get_despesas(response:Response, request:Request):
    return get_despesas_use_case.execute(response, request)
from repositories.despesas_repository import DespesaRepository
from .create_despesa_dto import CreateDespesaDTO
from .create_despesa_use_case import CreateDespesaUseCase   
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_despesa_use_case = CreateDespesaUseCase(DespesaRepository())

@router.post("/user/create-despesa")
def create_meeting(create_depsa_dto:CreateDespesaDTO, response:Response, request:Request):
    return create_despesa_use_case.execute(create_depsa_dto, response, request)
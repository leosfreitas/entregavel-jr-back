from repositories.despesas_repository import DespesaRepository
from fastapi import APIRouter, Request, Response, Depends
from use_cases.appraiser.edit_despesa.edit_despesa_use_case import EditDespesaUseCase
from .edit_despesa_dto import EditDespesaDTO
from middlewares.validate_appraiser_auth_token import validade_appraiser_auth_token

router = APIRouter()

expenses_repository = DespesaRepository()
edit_expense_use_case = EditDespesaUseCase(expenses_repository)

@router.put("/user/edit-despesa/{expense_id}", dependencies=[Depends(validade_appraiser_auth_token)])
def edit_expense(expense_id: str, edit_expense_dto: EditDespesaDTO, response: Response, request: Request):
    return edit_expense_use_case.execute(expense_id, edit_expense_dto, response, request)

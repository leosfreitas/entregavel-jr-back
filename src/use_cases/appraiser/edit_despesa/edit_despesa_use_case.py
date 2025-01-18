from repositories.despesas_repository import DespesaRepository
from .edit_despesa_dto import EditDespesaDTO
from fastapi import Request, Response
from bson import ObjectId

class EditDespesaUseCase:
    def __init__(self, despesa_repository: DespesaRepository):
        self.despesa_repository = despesa_repository

    def execute(self, expense_id: str, edit_expense_dto: EditDespesaDTO, response: Response, request: Request):
        if not ObjectId.is_valid(expense_id):
            response.status_code = 400
            return {"status": "error", "message": "ID de despesa inválido."}

        if not edit_expense_dto.tipo or not edit_expense_dto.valor:
            response.status_code = 406
            return {"status": "error", "message": "Falta informações obrigatórias para editar a despesa."}

        self.despesa_repository.update_despesa(
            despesa_id=expense_id,
            tipo=edit_expense_dto.tipo,
            valor=edit_expense_dto.valor,
            data=edit_expense_dto.data,
            descricao=edit_expense_dto.descricao
        )

        response.status_code = 202
        return {"status": "success", "message": "Despesa atualizada com sucesso."}

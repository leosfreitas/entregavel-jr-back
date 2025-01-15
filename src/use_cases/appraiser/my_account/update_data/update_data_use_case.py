from repositories.appraiser_repository import AppraisersRepository
from use_cases.appraiser.my_account.update_data.update_data_dto import UpdateDataDTO
from fastapi import Request, Response

class UpdateDataUseCase:
    appraiser_repository = AppraisersRepository

    def __init__(self, appraiser_repository: AppraisersRepository):
        self.appraiser_repository = appraiser_repository

    def execute(self, update_data_dto: UpdateDataDTO, response: Response, request: Request):
        appraiser_id = request.state.auth_payload["appraiser_id"]
        if not update_data_dto.name or not update_data_dto.email or not update_data_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Alteração não realizada, pois falta informações"}

        self.appraiser_repository.update_pwd(appraiser_id, update_data_dto.password)
        self.appraiser_repository.update_name(appraiser_id, update_data_dto.name)
        self.appraiser_repository.update_email(appraiser_id, update_data_dto.email)

        response.status_code = 202
        return{"status": "success", "message": "Atualização do cadastro realizado com sucesso"}
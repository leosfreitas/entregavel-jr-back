from repositories.director_repository import DirectorsRepository
from use_cases.director.my_account.update_data.update_data_dto import UpdateDataDTO
from fastapi import Request, Response

class UpdateDataUseCase:
    director_repository = DirectorsRepository

    def __init__(self, director_repository: DirectorsRepository):
        self.director_repository = director_repository

    def execute(self, update_data_dto: UpdateDataDTO, response: Response, request: Request):
        director_id = request.state.auth_payload["director_id"]
        if not update_data_dto.name or not update_data_dto.email or not update_data_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Alteração não realizada, pois falta informações"}

        self.director_repository.update_pwd(director_id, update_data_dto.password)
        self.director_repository.update_name(director_id, update_data_dto.name)
        self.director_repository.update_email(director_id, update_data_dto.email)

        response.status_code = 202
        return{"status": "success", "message": "Atualização do cadastro realizado com sucesso"}
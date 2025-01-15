from repositories.appraiser_repository import AppraisersRepository
from use_cases.appraiser.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.appraiser import Appraiser

class RegisterUseCase:
    appraiser_repository = AppraisersRepository

    def __init__(self, appraiser_repository: AppraisersRepository):
        self.appraiser_repository = appraiser_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        appraiser = Appraiser(**register_dto.model_dump())

        self.appraiser_repository.save(appraiser)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do avaliador com sucesso"}
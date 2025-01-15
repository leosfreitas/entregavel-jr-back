from repositories.director_repository import DirectorsRepository
from use_cases.director.auth.register.register_dto import RegisterDTO
from fastapi import Request, Response
from entities.director import Director

class RegisterUseCase:
    director_repository = DirectorsRepository

    def __init__(self, director_repository: DirectorsRepository):
        self.director_repository = director_repository

    def execute(self, register_dto: RegisterDTO, response: Response, request: Request):
        if not register_dto.name or not register_dto.email or not register_dto.password:
            response.status_code = 406
            return{"status": "error", "message": "Cadastro não realizado, pois falta informações"}

        director = Director(**register_dto.model_dump())

        self.director_repository.save(director)

        response.status_code = 201

        return{"status": "success", "message": "Cadastro do diretor com sucesso"}
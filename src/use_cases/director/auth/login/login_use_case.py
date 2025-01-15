from repositories.director_repository import DirectorsRepository
from fastapi import FastAPI, Request, Response
from use_cases.director.auth.login.login_dto import LoginDTO
from entities.director import Director
import jwt
import os

class LoginUseCase:
    director_repository: DirectorsRepository

    def __init__(self, director_repository: DirectorsRepository):
        self.director_repository = director_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        check_exists = self.director_repository.find_by_email(email=login_dto.email)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar um diretor com o email fornecido"}

        director = check_exists[0]

        if (not director.check_password_matches(login_dto.password)):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}

        token = jwt.encode({"email": director.email, "id": str(director.id)}, os.getenv("DIRECTOR_JWT_SECRET"))

        response.set_cookie(key="director_auth_token", value=f"Bearer {token}", httponly=True)
        
        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}
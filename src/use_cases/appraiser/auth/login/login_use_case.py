from repositories.appraiser_repository import AppraisersRepository
from fastapi import FastAPI, Request, Response
from use_cases.appraiser.auth.login.login_dto import LoginDTO
from entities.appraiser import Appraiser
import jwt
import os

class LoginUseCase:
    appraiser_repository: AppraisersRepository

    def __init__(self, appraiser_repository: AppraisersRepository):
        self.appraiser_repository = appraiser_repository

    def execute(self, login_dto: LoginDTO, response: Response, request: Request):
        check_exists = self.appraiser_repository.find_by_email(email=login_dto.email)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar um avaliador com o email fornecido"}

        appraiser = check_exists[0]

        if (not appraiser.check_password_matches(login_dto.password)):
            response.status_code = 400
            return {"status": "error", "message": "Senha incorreta, tente novamente mais tarde."}

        token = jwt.encode({"email": appraiser.email, "id": str(appraiser.id)}, os.getenv("APPRAISER_JWT_SECRET"))

        response.set_cookie(key="appraiser_auth_token", value=f"Bearer {token}", httponly=True)
        
        response.status_code = 202
        return {"status": "success", "message": "Acesso permitido"}
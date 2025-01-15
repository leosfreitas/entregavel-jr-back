from use_cases.director.auth.login.login_use_case import LoginUseCase
from repositories.director_repository import DirectorsRepository
from fastapi import FastAPI, Request, Response
from use_cases.director.auth.login.login_dto import LoginDTO
from fastapi import APIRouter

router = APIRouter()

director_repository = DirectorsRepository()
login_use_case = LoginUseCase(director_repository)

@router.post("/director/auth/login")
def director_login(director_login_dto: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(director_login_dto, response, request)
    
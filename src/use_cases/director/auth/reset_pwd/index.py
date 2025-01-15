from repositories.director_repository import DirectorsRepository
from fastapi import FastAPI, Request, Response
from use_cases.director.auth.reset_pwd.reset_pwd_use_case import ResetPwdUseCase
from use_cases.director.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO
from fastapi import APIRouter

router = APIRouter()

director_repository = DirectorsRepository()
reset_pwd_use_case = ResetPwdUseCase(director_repository)

@router.post("/director/auth/reset/pwd")
def reset_pwd(reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
    return reset_pwd_use_case.execute(reset_pwd_dto, response, request)
    
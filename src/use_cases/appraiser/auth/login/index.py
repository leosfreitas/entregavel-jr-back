from use_cases.appraiser.auth.login.login_use_case import LoginUseCase
from repositories.appraiser_repository import AppraisersRepository
from fastapi import FastAPI, Request, Response
from use_cases.appraiser.auth.login.login_dto import LoginDTO
from fastapi import APIRouter

router = APIRouter()

appraiser_repository = AppraisersRepository()
login_use_case = LoginUseCase(appraiser_repository)

@router.post("/appraiser/auth/login")
def appraiser_login(appraiser_login_dto: LoginDTO, response: Response, request: Request):
    return login_use_case.execute(appraiser_login_dto, response, request)
from repositories.appraiser_repository import AppraisersRepository
from fastapi import FastAPI, Request, Response
from use_cases.appraiser.auth.reset_pwd.reset_pwd_use_case import ResetPwdUseCase
from use_cases.appraiser.auth.reset_pwd.reset_pwd_dto import ResetPwdDTO
from fastapi import APIRouter

router = APIRouter()

appraiser_repository = AppraisersRepository()
reset_pwd_use_case = ResetPwdUseCase(appraiser_repository)

@router.post("/appraiser/auth/reset/pwd")
def reset_pwd(reset_pwd_dto: ResetPwdDTO, response: Response, request: Request):
    return reset_pwd_use_case.execute(reset_pwd_dto, response, request)
    
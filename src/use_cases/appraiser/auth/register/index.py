from use_cases.appraiser.auth.register.register_use_case import RegisterUseCase
from repositories.appraiser_repository import AppraisersRepository
from fastapi import FastAPI, Request, Response
from use_cases.appraiser.auth.register.register_dto import RegisterDTO
from fastapi import APIRouter

router = APIRouter()

appraiser_repository = AppraisersRepository()
doctor_register_use_case = RegisterUseCase(appraiser_repository)

@router.post("/appraiser/auth/register")
def appraiser_register(register_dto: RegisterDTO, response: Response, request: Request):
    return doctor_register_use_case.execute(register_dto, response, request)
    
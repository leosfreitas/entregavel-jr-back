from use_cases.director.auth.register.register_use_case import RegisterUseCase
from repositories.director_repository import DirectorsRepository
from fastapi import FastAPI, Request, Response
from use_cases.director.auth.register.register_dto import RegisterDTO
from fastapi import APIRouter

router = APIRouter()

director_repository = DirectorsRepository()
doctor_register_use_case = RegisterUseCase(director_repository)

@router.post("/director/auth/register")
def director_register(register_dto: RegisterDTO, response: Response, request: Request):
    return doctor_register_use_case.execute(register_dto, response, request)
    
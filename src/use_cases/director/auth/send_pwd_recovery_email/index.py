from repositories.director_repository import DirectorsRepository
from fastapi import FastAPI, Request, Response
from use_cases.director.auth.send_pwd_recovery_email.send_pwd_recovery_email_use_case import SendPwdRecoveryEmailUseCase
from use_cases.director.auth.send_pwd_recovery_email.send_pwd_recovery_email_dto import SendPwdRecoveryEmailDTO
from fastapi import APIRouter

router = APIRouter()

director_repository = DirectorsRepository()
send_pwd_recovery_email_use_case = SendPwdRecoveryEmailUseCase(director_repository)

@router.post("/director/auth/pwd/recovery/email")
def send_pwd_recovery_email(send_pwd_recovery_email_dto: SendPwdRecoveryEmailDTO, response: Response, request: Request):
    return send_pwd_recovery_email_use_case.execute(send_pwd_recovery_email_dto, response, request)
    
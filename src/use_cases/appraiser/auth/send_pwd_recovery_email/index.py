from repositories.appraiser_repository import AppraisersRepository
from fastapi import FastAPI, Request, Response
from use_cases.appraiser.auth.send_pwd_recovery_email.send_pwd_recovery_email_use_case import SendPwdRecoveryEmailUseCase
from use_cases.appraiser.auth.send_pwd_recovery_email.send_pwd_recovery_email_dto import SendPwdRecoveryEmailDTO
from fastapi import APIRouter

router = APIRouter()

appraiser_repository = AppraisersRepository()
send_pwd_recovery_email_use_case = SendPwdRecoveryEmailUseCase(appraiser_repository)

@router.post("/appraiser/auth/pwd/recovery/email")
def send_pwd_recovery_email(send_pwd_recovery_email_dto: SendPwdRecoveryEmailDTO, response: Response, request: Request):
    return send_pwd_recovery_email_use_case.execute(send_pwd_recovery_email_dto, response, request)
    
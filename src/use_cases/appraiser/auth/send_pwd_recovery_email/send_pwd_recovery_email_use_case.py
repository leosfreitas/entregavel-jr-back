from repositories.appraiser_repository import AppraisersRepository
from fastapi import Request, Response
from use_cases.appraiser.auth.send_pwd_recovery_email.send_pwd_recovery_email_dto import SendPwdRecoveryEmailDTO
from datetime import datetime
from utils.send_email import send_email
import uuid
from config.config import config

class SendPwdRecoveryEmailUseCase:
    appraiser_repository: AppraisersRepository

    def __init__(self, appraiser_repository: AppraisersRepository):
        self.appraiser_repository = appraiser_repository

    def execute(self, send_pwd_recovery_email_dto: SendPwdRecoveryEmailDTO, response: Response, request: Request):
        check_exists = self.appraiser_repository.find_by_email(email=send_pwd_recovery_email_dto.email)

        if (len(check_exists) == 0):
            response.status_code = 404
            return {"status": "error", "message": "Não foi possível achar o diretor com o email fornecido"}

        appraiser = check_exists[0]

        if appraiser.reset_pwd_token_sent_at + 3600 > datetime.now().timestamp():
            response.status_code = 400
            return {"status": "error", "message": "Você pode solicitar o link para redefinir sua senha a cada 1 hora."} 
        
        token = str(uuid.uuid4())

        self.appraiser_repository.update_reset_pwd_token(email=appraiser.email, sent_at=datetime.now().timestamp(), token=token)
        
        send_email(
            email=appraiser.email, 
            content=f"""
                <a href="{config["client_url"] + "/appraiser/password-recovery/" + token}">Redefina sua senha da conta clicando aqui:</a>
            """,
            subject="Link de redefinição de senha"
        )

        response.status_code = 200
        return {"status": "success", "message": "Link de redefinição de senha enviado com sucesso"}
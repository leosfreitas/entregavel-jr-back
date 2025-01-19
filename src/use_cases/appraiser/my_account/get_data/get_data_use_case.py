from repositories.appraiser_repository import AppraisersRepository
from fastapi import Request, Response

class getAppraiserData:
    def __init__(self, appraiser_repository: AppraisersRepository) -> None:
        self.appraiser_repository = appraiser_repository

    def execute(self, response: Response, request: Request):
        appraiser_id = request.state.auth_payload["appraiser_id"]
        appraiser_name = self.appraiser_repository.get_name(appraiser_id)
        appraiser_email = self.appraiser_repository.get_email(appraiser_id)
        appraiser_cpf = self.appraiser_repository.get_cpf(appraiser_id)
        appraiser_phone = self.appraiser_repository.get_phone(appraiser_id)

        return {"status":"success", "data": {"name": appraiser_name, 
                                             "email": appraiser_email, 
                                             "cpf": appraiser_cpf,
                                             "phone": appraiser_phone,
                                             "id": appraiser_id}}
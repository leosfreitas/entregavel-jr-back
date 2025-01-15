from repositories.appraiser_repository import AppraisersRepository
from fastapi import Request, Response

class getAppraiserName:
    def __init__(self, appraiser_repository: AppraisersRepository) -> None:
        self.appraiser_repository = appraiser_repository

    def execute(self, response: Response, request:Request):
        appraiser_id = request.state.auth_payload["appraiser_id"]
        appraiser_name = self.appraiser_repository.get_name(appraiser_id)

        return {"status":"success", "appraiser_name":appraiser_name}
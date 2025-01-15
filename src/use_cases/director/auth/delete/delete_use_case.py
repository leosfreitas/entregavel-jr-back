from repositories.appraiser_repository import AppraisersRepository
from fastapi import Request, Response

class DeleteAppraiserUseCase:
    def __init__(self, appraisers_repository: AppraisersRepository):
        self.appraisers_repository = appraisers_repository

    def execute(self, appraiser_id: str, response: Response, request: Request):
        print(appraiser_id)
        appraiser = self.appraisers_repository.find_by_id(appraiser_id)
        try:
            appraiser.delete()
            response.status_code = 204  
            return {"status": "success", "message": "Avaliador deletado com sucesso"}
        except Exception as e:
            response.status_code = 404  
            return {"status": "error", "message": "erro ao deletar avaliador"}
from repositories.appraiser_repository import AppraisersRepository
from fastapi import FastAPI, Request, Response, APIRouter, Depends
from .delete_use_case import DeleteAppraiserUseCase
from middlewares.validate_director_auth_token import validade_director_auth_token

router = APIRouter()

appraisers_repository = AppraisersRepository()
delete_appraiser_use_case = DeleteAppraiserUseCase(appraisers_repository)

@router.delete("/director/delete/{appraiser_id}", dependencies=[Depends(validade_director_auth_token)])
def delete_appraiser(appraiser_id: str, response: Response, request: Request):
    return delete_appraiser_use_case.execute(appraiser_id, response, request)
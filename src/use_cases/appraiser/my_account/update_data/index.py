from repositories.appraiser_repository import AppraisersRepository
from fastapi import FastAPI, Request, Response
from .update_data_use_case import UpdateDataUseCase
from .update_data_dto import UpdateDataDTO
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_appraiser_auth_token import validade_appraiser_auth_token

router = APIRouter()

appraiser_repository = AppraisersRepository()
update_data_use_case = UpdateDataUseCase(appraiser_repository)

@router.put("/appraiser/update/data", dependencies=[Depends(validade_appraiser_auth_token)])
def updata_data(update_data_dto: UpdateDataDTO, response: Response, request: Request):
    return update_data_use_case.execute(update_data_dto, response, request)

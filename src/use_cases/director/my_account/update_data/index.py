from repositories.director_repository import DirectorsRepository
from fastapi import FastAPI, Request, Response
from .update_data_use_case import UpdateDataUseCase
from .update_data_dto import UpdateDataDTO
from fastapi import APIRouter, Request, Response, Depends
from middlewares.validate_director_auth_token import validade_director_auth_token

router = APIRouter()

director_repository = DirectorsRepository()
update_data_use_case = UpdateDataUseCase(director_repository)

@router.put("/director/update/data", dependencies=[Depends(validade_director_auth_token)])
def updata_data(update_data_dto: UpdateDataDTO, response: Response, request: Request):
    return update_data_use_case.execute(update_data_dto, response, request)

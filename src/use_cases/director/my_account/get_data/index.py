from use_cases.director.my_account.get_data.get_data_use_case import getDirectorData
from repositories.director_repository import DirectorsRepository
from middlewares.validate_director_auth_token import validade_director_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

director_repository = DirectorsRepository()

get_data_use_case = getDirectorData(director_repository)

@router.get("/director/data", dependencies=[Depends(validade_director_auth_token)])
def get_director_data(response: Response, request:Request):
    return get_data_use_case.execute(response,request)
from use_cases.director.headbar.get_director_name_use_case import getDirectorName
from repositories.director_repository import DirectorsRepository
from middlewares.validate_director_auth_token import validade_director_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

director_repository = DirectorsRepository()

get_director_name_use_case = getDirectorName(director_repository)

@router.get("/director/headbar", dependencies=[Depends(validade_director_auth_token)])
def get_director_name(response: Response, request:Request):
    return get_director_name_use_case.execute(response,request)
from use_cases.appraiser.headbar.get_appraiser_name_use_case import getAppraiserName
from repositories.appraiser_repository import AppraisersRepository
from middlewares.validate_appraiser_auth_token import validade_appraiser_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

appraiser_repository = AppraisersRepository()

get_appraiser_name_use_case = getAppraiserName(appraiser_repository)

@router.get("/appraiser/headbar", dependencies=[Depends(validade_appraiser_auth_token)])
def get_appraiser_name(response: Response, request:Request):
    return get_appraiser_name_use_case.execute(response,request)
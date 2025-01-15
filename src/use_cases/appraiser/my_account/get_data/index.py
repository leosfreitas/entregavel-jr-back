from use_cases.appraiser.my_account.get_data.get_data_use_case import getAppraiserData
from repositories.appraiser_repository import AppraisersRepository
from middlewares.validate_appraiser_auth_token import validade_appraiser_auth_token
from fastapi import APIRouter, Request, Response, Depends

router = APIRouter()

appraiser_repository = AppraisersRepository()

get_data_use_case = getAppraiserData(appraiser_repository)

@router.get("/appraiser/data", dependencies=[Depends(validade_appraiser_auth_token)])
def get_appraiser_data(response: Response, request:Request):
    return get_data_use_case.execute(response,request)
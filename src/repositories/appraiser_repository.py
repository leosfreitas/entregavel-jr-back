import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.appraiser import Appraiser
from models.appraiser_model import AppraisersModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class AppraisersRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, appraiser: Appraiser) -> None:
        appraiser_model = AppraisersModel()
        appraiser_dict = appraiser.model_dump()

        for k in AppraisersModel.get_normal_fields():
            if (k not in appraiser_dict):
                continue

            appraiser_model[k] = appraiser_dict[k]

        for k in AppraisersModel.sensivity_fields:
            appraiser_model[k] = SensivityField(fernet=self.fernet, data=appraiser_dict[k])

        appraiser_model.password = bcrypt.hashpw(f'{appraiser.password}'.encode(), bcrypt.gensalt()).decode()

        appraiser_model.save()

        return None
    
    def find_by_email(self, email: str) -> list[AppraisersModel]:
        result = AppraisersModel.objects(email=email)
        return result
    
    def find_by_id(self, id: str) -> list[AppraisersModel]:
        result = AppraisersModel.objects(id=id)
        return result
    
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        AppraisersModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None
    
    def find_by_reset_pwd_token(self, token) -> list[AppraisersModel]:
        result: list[AppraisersModel] = AppraisersModel.objects(reset_pwd_token=token)

        return result
    
    def update_pwd(self, id: str, pwd: str) -> None:
        AppraisersModel.objects(id=id).update(set__password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None
    
    def get_name(self, id: str) -> str:
        appraiser = AppraisersModel.objects(id=id).first()
        if appraiser:
            return appraiser.name

    def get_email(self, id: str) -> str:
        appraiser = AppraisersModel.objects(id=id).first()
        if appraiser:
            return appraiser.email
    
    def update_name(self, id: str, name: str) -> None:
        AppraisersModel.objects(id=id).update(set__name = name)
        return None

    def update_email(self, id: str, email: str) -> None:
        AppraisersModel.objects(id=id).update(set__email = email)
        return None
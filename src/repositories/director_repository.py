import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.director import Director
from models.director_model import DirectorsModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class DirectorsRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, director: Director) -> None:
        director_model = DirectorsModel()
        director_dict = director.model_dump()

        for k in DirectorsModel.get_normal_fields():
            if (k not in director_dict):
                continue

            director_model[k] = director_dict[k]

        for k in DirectorsModel.sensivity_fields:
            director_model[k] = SensivityField(fernet=self.fernet, data=director_dict[k])

        director_model.password = bcrypt.hashpw(f'{director.password}'.encode(), bcrypt.gensalt()).decode()

        director_model.save()

        return None
    
    def find_by_email(self, email: str) -> list[DirectorsModel]:
        result = DirectorsModel.objects(email=email)
        return result
    
    def find_by_id(self, id: str) -> list[DirectorsModel]:
        result = DirectorsModel.objects(id=id)
        return result
    
    def update_reset_pwd_token(self, email: str, sent_at: int, token: str) -> None:
        DirectorsModel.objects(email=email).update(set__reset_pwd_token_sent_at=sent_at, set__reset_pwd_token=token)

        return None
    
    def find_by_reset_pwd_token(self, token) -> list[DirectorsModel]:
        result: list[DirectorsModel] = DirectorsModel.objects(reset_pwd_token=token)

        return result
    
    def update_pwd(self, id: str, pwd: str) -> None:
        DirectorsModel.objects(id=id).update(set__password = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode())

        return None
    
    def get_name(self, id: str) -> str:
        director = DirectorsModel.objects(id=id).first()
        if director:
            return director.name

    def get_email(self, id: str) -> str:
        director = DirectorsModel.objects(id=id).first()
        if director:
            return director.email
    
    def update_name(self, id: str, name: str) -> None:
        DirectorsModel.objects(id=id).update(set__name = name)
        return None

    def update_email(self, id: str, email: str) -> None:
        DirectorsModel.objects(id=id).update(set__email = email)
        return None
import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.despesa import Despesa
from models.despesa_model import DespesaModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class DespesaRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, despesa: Despesa) -> None:
        despesa_model = DespesaModel()
        despesa_dict = despesa.model_dump()

        for k in DespesaModel.get_normal_fields():
            if k not in despesa_dict:
                continue

            despesa_model[k] = despesa_dict[k]

        for k in DespesaModel.sensivity_fields:
            despesa_model[k] = SensivityField(fernet=self.fernet, data=despesa_dict[k])

        despesa_model.save()

        return None

    def get_despesa_by_id(self, despesa_id: str) -> dict:
        despesa = DespesaModel.objects.with_id(despesa_id)
        if not despesa:
            return None
        despesa_dict = despesa.to_mongo().to_dict()
        despesa_dict['_id'] = str(despesa_dict['_id'])
        return despesa_dict

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
from bson import ObjectId

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
    
    def get_despesa_by_user_id(self, user: str) -> List[dict]:
        despesas = DespesaModel.objects(user=user)
        if not despesas:
            return None

        despesas_list = []
        for despesa in despesas:
            despesa_dict = despesa.to_mongo().to_dict()
            despesa_dict['_id'] = str(despesa_dict['_id'])  
            despesas_list.append(despesa_dict)
        
        return despesas_list
    
    def delete_despesa_by_id(self, despesa_id: str, user: str) -> bool:
        despesa = DespesaModel.objects.with_id(despesa_id)
        if not despesa:
            return False
        if despesa.user != user:
            return False
        despesa.delete()
        return True
    
    def update_despesa(self, despesa_id: str, tipo: str, valor: float, data: str, descricao: str) -> bool:
        if not ObjectId.is_valid(despesa_id):
            return False

        despesa_model = DespesaModel.objects.with_id(ObjectId(despesa_id))
        if not despesa_model:
            return False

        if tipo:
            despesa_model.tipo = tipo
        if valor:
            despesa_model.valor = valor
        if data:
            despesa_model.data = data
        if descricao:
            despesa_model.descricao = descricao

        despesa_model.save()
        return True
from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class DespesaModel(Document):
    sensivity_fields = [
    ]

    user = StringField(required=False)
    tipo = StringField(
        required=True,
        choices=[
            "Habitação",
            "Transporte",
            "Alimentação",
            "Saúde",
            "Educação",
            "Lazer",
            "Roupas",
            "Tecnologia",
            "Assinaturas e Serviços",
            "Investimentos",
            "Doações",
            "Impostos",
            "Dívidas",
            "Outros"
        ]
    )

    valor = StringField(required=True)
    data = StringField(required=True)
    descricao = StringField(required=False)

    def get_normal_fields():
        return [
            i
            for i in DespesaModel.__dict__.keys()
            if i[:1] != "_" and i != "sensivity_fields" and i not in DespesaModel.sensivity_fields
        ]

import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Despesa(BaseModel):
    _id: str
    user: str
    tipo: Literal[
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
    valor: str
    data: str
    descricao: str
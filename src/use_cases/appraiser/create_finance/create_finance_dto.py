from pydantic import BaseModel
from typing import Literal, Optional

class CreateFinanceDTO(BaseModel):
    categoria: Literal[
        "Receita",
        "Despesa"
    ]
    
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
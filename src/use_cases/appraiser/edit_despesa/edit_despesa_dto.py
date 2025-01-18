from pydantic import BaseModel
from typing import Literal, Optional

class EditDespesaDTO(BaseModel):
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
    valor: Optional[str]  
    data: Optional[str]  
    descricao: Optional[str]

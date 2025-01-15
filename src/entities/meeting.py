import dotenv
from pydantic import BaseModel
from typing import Literal, Optional, List
dotenv.load_dotenv()

class Meeting(BaseModel):
    _id: str
    director: str
    appraisers: List[str]
    status: Literal["agendada","finalizada"]
    subject: Optional[str]
    day: int
    month: int
    inicial_time: str
    final_time: Optional[str]
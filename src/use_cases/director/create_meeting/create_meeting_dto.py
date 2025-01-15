from pydantic import BaseModel
from typing import Literal, Optional

class CreateMeetingDTO(BaseModel):
    director: str
    appraisers: list[str]
    status: Literal["agendada","finalizada"]
    subject: Optional[str] = ""
    day: int
    month: int
    inicial_time: str
    final_time: Optional[str] = ""
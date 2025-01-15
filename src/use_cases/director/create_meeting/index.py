from repositories.meeting_repository import MeetingRepository
from .create_meeting_dto import CreateMeetingDTO
from .create_meeting_use_case import CreateMeetingUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_meeting_use_case = CreateMeetingUseCase(MeetingRepository())

@router.post("/director/create-meeting")
def create_meeting(create_meeting_dto:CreateMeetingDTO, response:Response, request:Request):
    return create_meeting_use_case.execute(create_meeting_dto, response, request)
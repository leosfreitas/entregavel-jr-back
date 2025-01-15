from repositories.meeting_repository import MeetingRepository
from .get_meeting_use_case import GetMeetingUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

get_meeting_use_case = GetMeetingUseCase(MeetingRepository())

@router.get("/director/get-meeting/{meeting_id}")
def get_meeting(meeting_id: str ,response:Response, request:Request):
    return get_meeting_use_case.execute(meeting_id,response, request)
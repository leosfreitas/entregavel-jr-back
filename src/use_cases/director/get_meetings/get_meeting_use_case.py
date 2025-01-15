from repositories.meeting_repository import MeetingRepository
from use_cases.director.create_meeting.create_meeting_dto import CreateMeetingDTO
from fastapi import Request, Response
from entities.meeting import Meeting

class GetMeetingUseCase:
    def __init__(self, meeting_repository: MeetingRepository):
        self.meeting_repository = meeting_repository

    def execute(self, meeting_id: str, response: Response, request: Request):

        meeting = self.meeting_repository.get_meeting_by_id(meeting_id)
        if not meeting:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 400
        return meeting
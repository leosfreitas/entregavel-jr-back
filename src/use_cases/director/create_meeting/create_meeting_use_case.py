from repositories.meeting_repository import MeetingRepository
from use_cases.director.create_meeting.create_meeting_dto import CreateMeetingDTO
from fastapi import Request, Response
from entities.meeting import Meeting

class CreateMeetingUseCase:
    def __init__(self, meeting_repository: MeetingRepository):
        self.meeting_repository = meeting_repository

    def execute(self, create_meeting_dto: CreateMeetingDTO, response: Response, request: Request):
        if not create_meeting_dto.director or not create_meeting_dto.appraisers or not create_meeting_dto.status or not create_meeting_dto.day or not create_meeting_dto.month or not create_meeting_dto.inicial_time:
            response.status_code = 407
            return {"status": "error", "message":"faltam informações"}

        meeting = Meeting(
            director=create_meeting_dto.director,
            appraisers=create_meeting_dto.appraisers,
            status=create_meeting_dto.status,
            subject=create_meeting_dto.subject,
            day= create_meeting_dto.day,
            month= create_meeting_dto.month,
            inicial_time=create_meeting_dto.inicial_time,
            final_time=create_meeting_dto.final_time
        )

        self.meeting_repository.save(meeting)
        response.status_code=400
        return {"status": "success", "message":"Reuniao criada"}

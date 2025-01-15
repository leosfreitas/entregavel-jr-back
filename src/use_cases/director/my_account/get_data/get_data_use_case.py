from repositories.director_repository import DirectorsRepository
from fastapi import Request, Response

class getDirectorData:
    def __init__(self, director_repository: DirectorsRepository) -> None:
        self.director_repository = director_repository

    def execute(self, response: Response, request: Request):
        director_id = request.state.auth_payload["director_id"]
        director_name = self.director_repository.get_name(director_id)
        director_email = self.director_repository.get_email(director_id)

        return {"status":"success", "data": {"name": director_name, "email": director_email}}
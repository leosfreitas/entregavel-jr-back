from repositories.director_repository import DirectorsRepository
from fastapi import Request, Response

class getDirectorName:
    def __init__(self, director_repository: DirectorsRepository) -> None:
        self.director_repository = director_repository

    def execute(self, response: Response, request:Request):
        director_id = request.state.auth_payload["director_id"]
        director_name = self.director_repository.get_name(director_id)

        return {"status":"success", "director_name":director_name}
import os
import bcrypt
import dotenv
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.meeting import Meeting
from models.meeting_model import MeetingModel
from models.fields.sensivity_field import SensivityField
from utils.encode_hmac_hash import encode_hmac_hash

class MeetingRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, meeting: Meeting) -> None:
        meeting_model = MeetingModel()
        meeting_dict = meeting.model_dump()

        for k in MeetingModel.get_normal_fields():
            if (k not in meeting_dict):
                continue

            meeting_model[k] = meeting_dict[k]

        for k in MeetingModel.sensivity_fields:
            meeting_model[k] = SensivityField(fernet=self.fernet, data=meeting_dict[k])

    

        meeting_model.save()

        return None
    
    def get_meeting_by_id(self, meeting_id: str) -> dict:
        meeting = MeetingModel.objects.with_id(meeting_id)
        if not meeting:
            return None
        meeting_dict = meeting.to_mongo().to_dict()
        meeting_dict['_id'] = str(meeting_dict['_id'])
        return meeting_dict
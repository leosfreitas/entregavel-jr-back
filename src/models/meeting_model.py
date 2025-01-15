from mongoengine import *
import datetime
from models.fields.sensivity_field import SensivityField
import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()
fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

class MeetingModel(Document):
    sensivity_fields = [
        
    ]

    director = StringField(required=True)
    appraisers = ListField(StringField(), required = True)
    status = StringField(required=True)
    subject = StringField()
    day = IntField(required=True)
    month = IntField(required=True)
    inicial_time = StringField(required=True)
    final_time = StringField()

    



    def get_normal_fields():
        return [i for i in MeetingModel.__dict__.keys() if i[:1] != '_' and i != "sensivity_fields" and i not in MeetingModel.sensivity_fields]
    

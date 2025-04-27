
# Create your tests here.
from datetime import date

from ninja import Schema
from pydantic import BaseModel


class StatusSchema(Schema):
    status: str

class FormIn(BaseModel):
    seed: str
    metodo_plantio: str
    irrigacao: str
    solo: str
    data_inicio: date

class taskOut(Schema):
    task: str
    start: date
    end: date
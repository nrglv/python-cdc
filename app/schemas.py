from pydantic import BaseModel

class RecordBase(BaseModel):
    name: str
    description: str

class RecordCreate(RecordBase):
    pass

class RecordUpdate(RecordBase):
    pass

class Record(RecordBase):
    id: int

    class Config:
        orm_mode = True

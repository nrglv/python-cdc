from sqlalchemy.orm import Session
from models import User, Record 
from schemas import RecordCreate, RecordUpdate

def create_record(db: Session, record: RecordCreate):
    db_record = Record(name=record.name, description=record.description)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def update_record(db: Session, record_id: int, record: RecordUpdate):
    db_record = db.query(Record).filter(Record.id == record_id).first()
    if db_record:
        db_record.name = record.name
        db_record.description = record.description
        db.commit()
        db.refresh(db_record)
    return db_record

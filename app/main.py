from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
import database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/records/", response_model=schemas.Record)
def create_record(record: schemas.RecordCreate, db: Session = Depends(database.get_db)):
    return crud.create_record(db=db, record=record)

@app.put("/records/{record_id}", response_model=schemas.Record)
def update_record(record_id: int, record: schemas.RecordUpdate, db: Session = Depends(database.get_db)):
    db_record = crud.update_record(db=db, record_id=record_id, record=record)
    if db_record is None:
        raise HTTPException(status_code=404, detail="Record not found")
    return db_record

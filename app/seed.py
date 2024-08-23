from sqlalchemy.orm import Session
from models import Record
from database import SessionLocal

def generate_records(db: Session, count: int = 100):
    for i in range(count):
        record = Record(
            name=f"Record {i + 1}",
            description=f"Description for record {i + 1}"
        )
        db.add(record)
    db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    generate_records(db)
    db.close()

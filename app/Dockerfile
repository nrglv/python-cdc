FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app
WORKDIR /app


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN alembic upgrade head 

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & python seed.py && tail -f /dev/null"]

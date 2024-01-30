FROM python:3.12

RUN mkdir -p /app

COPY models /app/models
COPY requirements.txt /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "models/FastAPI.py"]
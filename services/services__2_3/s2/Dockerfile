FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY project/__init__.py /app/project/__init__.py
COPY project/services/__init__.py /app/project/services/__init__.py

COPY project/services/services__2_3 /app/project/services/services__2_3
COPY project/kafka_app /app/project/kafka_app

CMD ["python", "-m", "project.services.services__2_3.s2.main"]

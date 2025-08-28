FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# נוסיף רק את מה שצריך
COPY project/__init__.py /app/project/__init__.py
COPY project/services/__init__.py /app/project/services/__init__.py

# נעתיק service_1_4 (בשביל DALMongo)
COPY project/services/service_1_4 /app/project/services/service_1_4

# נעתיק kafka_app (בשביל KafkaDAL)
COPY project/kafka_app /app/project/kafka_app

# נעתיק את קבצי s4 עצמם (main + persister)
COPY project/services/services__2_3/s4 /app/project/services/services__2_3/s4

# נקודת כניסה
CMD ["python", "-m", "project.services.services__2_3.s4.main"]

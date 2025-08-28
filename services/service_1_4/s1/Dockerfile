FROM python:3.10-slim

WORKDIR /app

# dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy packages
COPY project/__init__.py /app/project/__init__.py
COPY project/services/__init__.py /app/project/services/__init__.py
COPY project/services/service_1_4/__init__.py /app/project/services/service_1_4/__init__.py

COPY project/services/service_1_4/fech_mongo /app/project/services/service_1_4/fech_mongo
COPY project/services/service_1_4/s1 /app/project/services/service_1_4/s1
COPY project/kafka_app /app/project/kafka_app

# run
CMD ["python", "-m", "project.services.service_1_4.s1.main"]

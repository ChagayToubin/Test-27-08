FROM python:3.10-slim

# תיקיית עבודה
WORKDIR /app

# התקנת תלויות
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# נעתיק רק את הקבצים שאתה צריך
COPY project/__init__.py /app/project/__init__.py
COPY project/services/__init__.py /app/project/services/__init__.py

# נעתיק את כל השירות services__2_3 (כולל s2 ו-s3 בפנים)
COPY project/services/services__2_3 /app/project/services/services__2_3

# נוסיף kafka_app
COPY project/kafka_app /app/project/kafka_app

# נוריד מראש את ה-vader lexicon בשביל NLTK

# נקודת כניסה להרצה (כמו בדוגמה שלך)
CMD ["python", "-m", "project.services.services__2_3.s3.main"]

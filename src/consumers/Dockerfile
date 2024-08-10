FROM python:3.9-slim

WORKDIR /app

# Copy requirements.txt from the build context
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary files
COPY src/consumers/weather_consumer.py .

CMD ["python", "weather_consumer.py"]

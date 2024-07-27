# src/consumers/weather_consumer.py
from kafka import KafkaConsumer
import json

def consume_weather_data():
    consumer = KafkaConsumer(
        'weather_topic',
        bootstrap_servers=['localhost:29092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='weather-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for message in consumer:
        weather_data = message.value
        print(f"Data received: {weather_data}")
        # Process the weather data here

if __name__ == "__main__":
    consume_weather_data()

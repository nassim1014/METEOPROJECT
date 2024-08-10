import requests
import json
from kafka import KafkaProducer
import requests
import time
# Configuration de l'API
API_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/france?unitGroup=metric&key=JRADSM3HCV7QFDWEWDWMEKTGD&contentType=json'
API_KEY = 'JRADSM3HCV7QFDWEWDWMEKTGD'

def fetch_weather_data():
    response = requests.get(API_URL, params={'apikey': API_KEY})
    data = response.json()
    return data

def produce_weather_data():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    while True:
        weather_data = fetch_weather_data()
        producer.send('weather_topic', weather_data)
        print(f"Data sent: {weather_data}")
        time.sleep(300)  # Attendre 5 minutes avant la prochaine requête

if __name__ == "__main__":
    print("producer running")
    produce_weather_data()
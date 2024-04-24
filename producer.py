from confluent_kafka import Producer
import json

# Initialize Kafka producer
producer_conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(producer_conf)

# Function to read preprocessed data and publish to Kafka topic
def publish_data_to_topic():
    with open('preprocessed_amazon_data.json', 'r') as f:
        for line in f:
            producer.produce('amazon_data_topic', value=line.strip())
            producer.poll(0)  # Trigger delivery report callback
    producer.flush()  # Wait for all messages to be delivered

# Publish preprocessed data to Kafka topic
publish_data_to_topic()

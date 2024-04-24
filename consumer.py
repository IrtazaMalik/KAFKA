from confluent_kafka import Consumer, KafkaError
import json

# Initialize Kafka consumer
consumer_conf = {'bootstrap.servers': 'localhost:9092', 'group.id': 'consumer_group'}
consumer = Consumer(consumer_conf)
consumer.subscribe(['amazon_data_topic'])  # Subscribe to the Kafka topic

# Function to consume data from Kafka topic
def consume_data_from_topic():
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        data = json.loads(msg.value().decode('utf-8'))  # Decode and load JSON data
        # Process data here based on consumer application's requirements
        print(data)

# Consume data from Kafka topic
consume_data_from_topic()

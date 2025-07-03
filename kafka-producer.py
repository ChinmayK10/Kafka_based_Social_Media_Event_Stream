import sys
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

# Kafka server configuration
KAFKA_SERVER = "localhost:9092"

# Get topic names from command-line arguments
topics = sys.argv[1:]

# Initialize Kafka Producer with error handling
try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_SERVER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print("[INFO] Connected to Kafka successfully!")
except KafkaError as e:
    print(f"[ERROR] Failed to connect to Kafka: {e}")
    sys.exit(1)

# Function to send messages to Kafka
def to_producer(topic, message):
    try:
        producer.send(topic, message)
        producer.flush()
        print(f"[INFO] Sent to {topic}: {message}")
    except KafkaError as e:
        print(f"[ERROR] Failed to send message to {topic}: {e}")

# Read input from stdin
for line in sys.stdin:
    line = line.strip()
    
    if line == 'EOF':
        message = {"type": "EOF"}
        for topic in topics:
            to_producer(topic, message)
        break

    message = {}
    words = line.split()

    if not words:
        continue  # Ignore empty lines

    action = words[0]
    
    if action == 'comment':
        message['type'] = 'comment'
        message["user_who_posted"] = words[2]
        message['comment'] = " ".join(words[4:]).strip('"')
        topics_send = [topics[0], topics[2]]

    elif action == 'like':
        message['type'] = 'like'
        message["user_who_posted"] = words[2]
        message['post_id'] = int(words[3])
        topics_send = [topics[1], topics[2]]

    elif action == 'share':
        message['type'] = 'share'
        message["user_who_posted"] = words[2]
        message['shared_to'] = words[4:]
        topics_send = [topics[2]]

    else:
        print(f"[WARNING] Unknown action: {action}")
        continue

    # Send message to Kafka topics
    for topic in topics_send:
        to_producer(topic, message)

# Final cleanup
print("[INFO] Finished sending messages.")
producer.flush()
producer.close()

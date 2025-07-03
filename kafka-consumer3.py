from kafka import KafkaConsumer
import json
import sys

topic_name = sys.argv[1]
consumer_settings = {
    'bootstrap_servers': 'localhost:9092',
    'group_id': 'shares',
    'auto_offset_reset': 'latest',
    'enable_auto_commit': True,
    'value_deserializer': lambda x: json.loads(x.decode('utf-8'))
}
consumer = KafkaConsumer(topic_name, **consumer_settings)

shares = {}

for message in consumer:
    data = message.value
    if data['type'] == 'share':
        user_who_posted = data['user_who_posted']
        shared_to = data['shared_to']
        shares.setdefault(user_who_posted, []).extend(shared_to)
    if data['type'] == 'EOF':
        break

print(json.dumps(shares, indent=4, sort_keys=True))

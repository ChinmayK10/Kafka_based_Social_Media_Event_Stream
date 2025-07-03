from kafka import KafkaConsumer
import json
import sys

# Specify the topic
topic_name = sys.argv[1]
consumer_settings = {
    'bootstrap_servers': 'localhost:9092',
    'group_id': 'comments',
    'auto_offset_reset': 'latest',
    'enable_auto_commit': True,
    'value_deserializer': lambda x: json.loads(x.decode('utf-8'))
}
consumer = KafkaConsumer(topic_name, **consumer_settings)

comments = {}
for message in consumer:
    data = message.value
    if data['type'] == 'comment':
        user_who_posted = data['user_who_posted']
        comments.setdefault(user_who_posted, []).append(data['comment'])
    if data['type'] == 'EOF':
        break

print(json.dumps(comments, indent=4, sort_keys=True))

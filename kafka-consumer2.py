from kafka import KafkaConsumer
import json
import sys

topic_name = sys.argv[1]
consumer_settings = {
    'bootstrap_servers': 'localhost:9092',
    'group_id': 'likes',
    'auto_offset_reset': 'latest',
    'enable_auto_commit': True,
    'value_deserializer': lambda x: json.loads(x.decode('utf-8'))
}
consumer = KafkaConsumer(topic_name, **consumer_settings)
likes = {}

for message in consumer:
    data = message.value
    if data['type'] == 'like':
        user_who_posted = data['user_who_posted']
        post_id = str(data['post_id'])
        likes.setdefault(user_who_posted, {}).setdefault(post_id, 0)
        likes[user_who_posted][post_id] += 1
    if data['type'] == 'EOF':
        break

print(json.dumps(likes, indent=4, sort_keys=True))

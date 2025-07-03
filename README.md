# Kafka_based_Social_Media_Event_Stream
Real-time social media event simulation using Apache Kafka and Python. Includes a CLI-based producer and dedicated consumers for comments, likes, and shares, demonstrating Kafka-based event streaming and message processing.
# Features
Kafka Producer that accepts:

comment by <user> "<text>"

like by <user> <post_id>

share by <user> to <user1> <user2> ...

Sends structured JSON messages to Kafka topics

Three dedicated Kafka Consumers to process:

Comments per user

Likes per user-post

Shares per user

EOF input cleanly stops all consumers

CLI-based real-time simulation

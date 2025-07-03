# Kafka-Social-Media-Analytics
## Overview
This project demonstrates a real-time social media event streaming system using Apache Kafka and Python. A Kafka producer streams user actions (comments, likes, shares), while three separate consumers handle data for analytics and reporting.

## Requirements
* Python 3.x
* Kafka-Python
* Apache Kafka running locally (localhost:9092)

## Project Structure
* producer.py: Sends user action events to Kafka topics
* consumer_comments.py: Handles and aggregates comments per user
* consumer_likes.py: Tracks number of likes per user per post
* consumer_shares.py: Aggregates share actions to track shared recipients

## How to Run
1. Start Kafka server.
    Make sure Kafka and Zookeeper are running on localhost:9092.
2. Create three Kafka topics
```bash
kafka-topics.sh --create --topic topicName1 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
kafka-topics.sh --create --topic topicName2 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
kafka-topics.sh --create --topic topicName3 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```
3. Run consumers:
```bash
python3 kafka-consumer1.py topicName1 topicName2 topicName3 > output1.json
python3 kafka-consumer2.py topicName1 topicName2 topicName3 > output2.json
python3 kafka-consumer3.py topicName1 topicName2 topicName3 > output3.json
```
4. Run the producer:
```bash
cat dataset.txt | python producer.py comment_topic like_topic share_topic
```

## Client Specific Outputs
* Client 1
List down all the comments received on posts for all users.

```sh
{
    "@username1" : [
        "comment1",
        "comment2"
    ],
    "@username2" : [
        "comment1",
        "comment2"
    ],
    ...
}
```
* Client 2
List down the number of likes received on different posts for each user.
```sh
{
    "@username1" : {
        "post-id-1" : no_of_likes,
        "post-id-2" : no_of_likes
    },
    ...
}
```
* Client 3
Calculate the popularity of a user based on the number of likes, shares, and comments on the user’s profile.
```sh
{
    "@username_1": popularity,
    "@username_2": popularity,
    ...
}
```
##Future Enhancements
* Persist output to MongoDB or PostgreSQL
* Add timestamps to each event
* Visualize with Flask/Streamlit dashboards
* Scale using topic partitions and Docker setup
```sh


import os
import json

from project.classes.fetchers.my_kafka.my_kafka_consumer.my_kafka_consumer import MyKafkaConsumer
from project.classes.fetchers.my_kafka.my_kafka_producer.my_kafka_producer import MyKafkaProducer
from project.classes.app_maneger.app_maneger import AppManager
from project.classes.message_builders.message_builder_preprocessor.message_builder_preprocessor import MessageBuilderPreprocessor


kafka_host_client = os.getenv("KAFKA_HOST", "localhost")
kafka_port_client = os.getenv("KAFKA_PORT", 9092)

topics_dal = os.getenv("TOPICS_DAL", 'raw_tweets_antisemitic,raw_tweets_not_antisemitic').split(',')
kafka_host_dal = os.getenv("KAFKA_HOST", "localhost")
kafka_port_dal = os.getenv("KAFKA_PORT", 9092)
group_id = os.getenv("GROUP_ID", "my-consumer")


topics_client = os.getenv("TOPICS_CLIENT", 'preprocessed_tweets_antisemitic,preprocessed_tweets_not_antisemitic').split(',')
configs_for_kafka_client = {
    'bootstrap_servers':[f"{kafka_host_client}:{kafka_port_client}"],
    'value_serializer': lambda v: json.dumps(v).encode("utf-8")
}


configs_for_kafka_dal = {
    'bootstrap_servers' : [f"{kafka_host_dal}:{kafka_port_dal}"],
    'group_id' : group_id,
    'auto_offset_reset' : "earliest",
    'enable_auto_commit' : 'True',
    'value_deserializer' : lambda v: json.loads(v.decode("utf-8"))
}

dal = MyKafkaConsumer(topics_dal, configs_for_kafka_dal)
client = MyKafkaProducer(configs_for_kafka_client)
data_builder = MessageBuilderPreprocessor


manager_app = AppManager(dal, client, data_builder, topics_client)
manager_app.manager()
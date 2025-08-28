import os
import json

from project.kafka_app.Consumer.kafka_con import KafkaDAL
from project.kafka_app.Producer.kafka_pro import KafkaClient
from project.services.services__2_3.core.app_maneger.app_maneger import AppManager
from project.services.services__2_3.s2.core.data_builder.data_builder import DataBuilder


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

dal = KafkaDAL(topics_dal, configs_for_kafka_dal)
client = KafkaClient(configs_for_kafka_client)
data_builder = DataBuilder


manager_app = AppManager(dal, client, data_builder, topics_client)
manager_app.manager()
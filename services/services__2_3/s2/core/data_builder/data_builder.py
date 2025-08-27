from kafka import KafkaConsumer
import kafka

from cleaner import Cleaner

class DataBuilder:

    @staticmethod
    def build(kafka_object : kafka.consumer.fetcher.ConsumerRecord):
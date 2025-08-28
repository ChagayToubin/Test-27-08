from project.services.services__2_3.core.cleaner.cleaner import Cleaner



class DataBuilder:

    @staticmethod
    def build(kafka_object, topic_client_names) -> dict:

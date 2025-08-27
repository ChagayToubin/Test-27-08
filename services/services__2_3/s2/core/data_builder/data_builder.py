from cleaner import Cleaner

class DataBuilder:

    @staticmethod
    def build(kafka_object) -> dict:
        topic_name = kafka_object.topic
        message = kafka_object.value
        clean_text = Cleaner.clean_text(message['text'])
        message['clean_text'] = clean_text
        return {'topic_name' : topic_name, 'message' : message}
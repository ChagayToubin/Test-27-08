from project.services.services__2_3.core.cleaner.cleaner import Cleaner

class DataBuilder:

    @staticmethod
    def build(kafka_object, topic_client_names) -> dict:
        topic_old_name = kafka_object.topic
        topic_new_name = DataBuilder.attaching_topic_name(topic_old_name, topic_client_names)
        message = kafka_object.value
        clean_text = Cleaner.clean_text(message['text'])
        message['clean_text'] = clean_text
        return {'topic_name' : topic_new_name, 'message' : message}


    @staticmethod
    def attaching_topic_name(topic_old_name, topic_new_names):
        _not__in_topic = 0
        if '_not_' in topic_new_names[1]:
            _not__in_topic = 1
        if '_not_' in topic_old_name:
                return topic_new_names[_not__in_topic]
        return topic_new_names[_not__in_topic - 1]



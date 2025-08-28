from project.services.services__2_3.core.cleaner.cleaner import Cleaner
from project.services.services__2_3.s3.core.dal.dal_file import DAL
from project.services.services__2_3.s3.core.data_builder.data_analyzer.data_analyzer import DataAnalyzer



class DataBuilder:

    @staticmethod
    def build(kafka_object, topic_client_names) -> dict:
        topic_old_name = kafka_object.topic
        topic_new_name = DataBuilder.attaching_topic_name(topic_old_name, topic_client_names)
        blacklist = DAL.load_file()
        blacklist = set(Cleaner.clean_text(blacklist).split())
        message = kafka_object.value
        clean_text = message['clean_text']
        message["sentiment"] = DataAnalyzer.classify_sentiment(clean_text)
        message["weapons_detected"] = ",".join(list(DataAnalyzer.find_words_in_blacklist(clean_text.split(), blacklist)))
        message['relevant_timestamp'] = DataAnalyzer.get_dates_in_text(message['text'])
        return {'topic_name': topic_new_name, 'message': message}


    @staticmethod
    def attaching_topic_name(topic_old_name, topic_new_names):
        _not__in_topic = 0
        if '_not_' in topic_new_names[1]:
            _not__in_topic = 1
        if '_not_' in topic_old_name:
                return topic_new_names[_not__in_topic]
        return topic_new_names[_not__in_topic - 1]
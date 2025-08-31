from project.classes.text_cleaner.text_cleaner import TextCleaner
from project.classes.fetchers.blacklist_dal.dal_blacklist import BlackListDAL
from project.classes.text_analyzer.text_analyzer import TextAnalyzer



class MessageBuilderEnricher:

    @staticmethod
    def build(kafka_object, topic_client_names) -> dict:
        topic_old_name = kafka_object.topic
        topic_new_name = MessageBuilderEnricher.attaching_topic_name(topic_old_name, topic_client_names)
        blacklist = BlackListDAL.load_file()
        blacklist = set(TextCleaner.clean_text(blacklist).split())
        message = kafka_object.value
        clean_text = message['clean_text']
        message["sentiment"] = TextAnalyzer.classify_sentiment(clean_text)
        message["weapons_detected"] = ",".join(list(TextAnalyzer.find_words_in_blacklist(clean_text.split(), blacklist)))
        message['relevant_timestamp'] = TextAnalyzer.get_dates_in_text(message['text'])
        return {'topic_name': topic_new_name, 'message': message}


    @staticmethod
    def attaching_topic_name(topic_old_name, topic_new_names):
        _not__in_topic = 0
        if '_not_' in topic_new_names[1]:
            _not__in_topic = 1
        if '_not_' in topic_old_name:
                return topic_new_names[_not__in_topic]
        return topic_new_names[_not__in_topic - 1]
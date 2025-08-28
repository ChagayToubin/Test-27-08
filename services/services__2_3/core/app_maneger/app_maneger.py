from project.kafka_app.Consumer.kafka_con import KafkaDAL
from project.kafka_app.Producer.kafka_pro import KafkaClient


class AppManager:

    def __init__(self, dal : KafkaDAL, client : KafkaClient, data_builder ,topic_client_names : list):
        self.dal = dal
        self.client = client
        self.topic_client_names = topic_client_names
        self.data_builder = data_builder


    def manager(self):
        try:
            self.dal.open()
            self.client.open()
            for msg in self.dal.consume():
                print("The pull from Kafka was successful.")
                data = self.data_builder.build(msg, self.topic_client_names)
                self.client.send_to_kapka(data['topic_name'], data['message'])
                print("'The sending was successful.")
        except Exception as e:
            print(type(e).__name__, "-", e)
        finally:
            self.dal.close()
            self.client.close()
from project.services.service_1_4.fech_mongo import DALMongo
from project.kafka_app.Consumer.kafka_con import KafkaDAL

class Persister:
    def __init__(self,HOST, DB, COLLECTION, USER, PASSWORD,kaf_config,topics):

        self.Mongo=DALMongo(HOST, DB, COLLECTION, USER, PASSWORD)

        self.kaf=KafkaDAL(topics,kaf_config)



    def pull_from_kafka(self):
        self.kaf.open()
        for i in self.kaf.consume():
            print(i.topic,"ssss")
            self.Mongo.enter_to_local_db(i.value,i.topic)







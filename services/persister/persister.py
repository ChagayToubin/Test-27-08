from project.classes.fetchers.my_mongodb.MongoBD import DALMongo
from project.classes.fetchers.my_kafka.my_kafka_consumer.my_kafka_consumer import MyKafkaConsumer

class Persister:
    def __init__(self,HOST, DB, COLLECTION, USER, PASSWORD,kaf_config,topics):

        self.Mongo=DALMongo(HOST, DB, COLLECTION, USER, PASSWORD)

        self.kaf=MyKafkaConsumer(topics, kaf_config)



    def pull_from_kafka(self):
        self.kaf.open()
        for i in self.kaf.consume():
            print(i.topic,"ssss")
            self.Mongo.enter_to_local_db(i.value,i.topic)







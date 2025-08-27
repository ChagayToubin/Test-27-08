from pymongo import MongoClient
import time
from project.kafka.Producer.kafka_pro import KafkaPro

class DALMongo:

    def __init__(self, host, database, collection, user, password, kaf_config):
        self.host = host
        self.database = database
        self.collection = collection
        self.user = user
        self.password = password
        self.URI = self.get_URI()
        self.client = None
        self.data = None
        self.kaf = KafkaPro(kaf_config)

    def get_URI(self):
        if self.user and self.password:
            URI = f"mongodb+srv://{self.user}:{self.password}@{self.host}/"
        else:
            URI = f"mongodb://{self.host}:27017"
        return URI

    def open_connection(self):
        try:
            self.client = MongoClient(self.URI)
            return True
        except Exception as e:
            print("Error: ", e)
            return False

    def close_connection(self):
        if self.client:
            self.client.close()

    def Dstart_pull_100_min(self):

        self.open_connection()
        db = self.client[self.database]
        collection = db[self.collection]
        last_date = None
        self.kaf.open()
        while True:
            query = {}
            if last_date:
                query = {"CreateDate": {"$gt": last_date}}
            docs = list(collection.find(query).sort("CreateDate", 1).limit(100))
            docs = DALMongo.correct_the_id(docs)
            if docs:
                for d in docs:
                    print(d)
                    self.check_raw_tweets_antisemitic_and_send(d)

                last_date = docs[-1]["CreateDate"]

            time.sleep(10)

    def check_raw_tweets_antisemitic_and_send(self, msg):

        if msg["Antisemitic"] == 1:
            self.kaf.send_to_kapka("raw_tweets_antisemitic", msg)
        else:
            self.kaf.send_to_kapka("raw_tweets_not_antisemitic", msg)


    @staticmethod
    def correct_the_id(result):
        for organ in result:
            organ['_id'] = str(organ['_id'])
            organ['CreateDate'] = str(organ['CreateDate'])

        return result

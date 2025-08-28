from pymongo import MongoClient
import time
from project.kafka_app.Producer.kafka_pro import proKafka


class DALMongo:

    def __init__(self, host, database, collection, user, password, kaf_config=None):
        self.host = host
        self.database = database
        self.collection = collection
        self.user = user
        self.password = password
        self.URI = self.get_URI()
        self.client = None
        self.data = None
        self.kaf = proKafka(kaf_config)

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
            docs = list(collection.find(query).sort("CreateDate", 1).limit(1))
            last_date = docs[-1]["CreateDate"]
            docs = DALMongo.correct_the_id(docs)
            if docs:
                for d in docs:
                    print(d)
                    self.check_raw_tweets_antisemitic_and_send(d)

            time.sleep(4)

    def check_raw_tweets_antisemitic_and_send(self, msg):
        if msg["Antisemitic"] == 1:
            self.kaf.send_to_kapka("raw_tweets_antisemitic", msg)
        else:
            self.kaf.send_to_kapka("raw_tweets_not_antisemitic", msg)

    def enter_to_local_db(self, data,topic):
        self.open_connection()
        db = self.client[self.database]
        collection_antisemtic = db["raw_tweets_antisemitic"]
        collection_not_antisemtic = db["raw_tweets_not_antisemitic"]
        data.pop("_id", None)

        if topic == "enriched_preprocessed_tweets_antisemitic":
            x = collection_antisemtic.insert_one(data)
        else:
            x = collection_not_antisemtic.insert_one(data)

    @staticmethod
    def correct_the_id(result):
        for organ in result:
            organ['_id'] = str(organ['_id'])
            organ['CreateDate'] = str(organ['CreateDate'])
        return result

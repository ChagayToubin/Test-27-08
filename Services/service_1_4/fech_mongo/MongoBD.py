from pymongo import MongoClient
import time
class DALMongo:

    def __init__(self, host, database, collection, user, password):
        self.host = host
        self.database = database
        self.collection = collection
        self.user = user
        self.password = password
        self.URI = self.get_URI()
        self.client = None
        self.data=None

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

    def get_all_100_min(self):

        self.open_connection()
        db = self.client[self.database]
        collection = db[self.collection]
        last_date = None
        while True:
            query = {}
            if last_date:
                query = {"CreateDate": {"$gt": last_date}}
            docs = list(collection.find(query).sort("CreateDate", 1).limit(100))
            if docs:
                for d in docs:
                    print(d)
                last_date = docs[-1]["CreateDate"]
            # לדחוף פו לקפקה
            time.sleep(60)


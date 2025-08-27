from pymongo import MongoClient
import time
#
from  Services.service_1_4.fech_mongo import DALMongo


class Retriever1:
    def __init__(self,HOST, DB, COLLECTION, USER, PASSWORD,kaf_config):
        self.Mongo=DALMongo(HOST, DB, COLLECTION, USER, PASSWORD,kaf_config)

    def Rstart_pull_100_min(self):
        self.Mongo.Dstart_pull_100_min()
        self.Mongo.kaf.close()

#
#



# # c=MongoClient("mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/")
#
#
def sdds():
    c = MongoClient("mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/")
    db = c["IranMalDB"]
    col = db["tweets"]
    last_date=None
    while True:
        query = {}
        if last_date:
            query = {"CreateDate": {"$gt": last_date}}

        docs = list(col.find(query).sort("CreateDate", 1).limit(100))

        if docs:
            for d in docs:
                print(type(d["Antisemitic"]))
            last_date = docs[-1]["CreateDate"]

        time.sleep(60)




# sdds()

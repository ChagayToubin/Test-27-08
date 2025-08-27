from pymongo import MongoClient
import time

import os
#
from  Services.service_1_4.fech_mongo import DALMongo

HOST = os.getenv("HOST", "cluster0.6ycjkak.mongodb.net")
USER = os.getenv("USER", "IRGC_NEW")
PASSWORD = os.getenv("PASSWORD", "iran135")
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "tweets")

class Retriever1:
    def __init__(self,HOST, DB, COLLECTION, USER, PASSWORD):
        self.Mongo=DALMongo(HOST, DB, COLLECTION, USER, PASSWORD)
        self.data=None
    def get_all_data_100_min(self):
        self.data=self.Mongo.get_all()

c=Retriever1(HOST, DB, COLLECTION, USER, PASSWORD)
c.get_all_data()

# # c=MongoClient("mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/")
#
#
# def sdds():
#     c = MongoClient("mongodb+srv://IRGC_NEW:iran135@cluster0.6ycjkak.mongodb.net/")
#     db = c["IranMalDB"]
#     col = db["tweets"]
#     last_date=None
#     while True:
#         query = {}
#         if last_date:
#             query = {"CreateDate": {"$gt": last_date}}
#
#         docs = list(col.find(query).sort("CreateDate", 1).limit(100))
#
#         if docs:
#             for d in docs:
#                 print(d)
#             last_date = docs[-1]["CreateDate"]
#
#         time.sleep(60)
#
#
#
#
# sdds()

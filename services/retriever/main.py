from project.services.retriever.Retriever import Retriever1
import os
import json
HOST = os.getenv("HOST", "cluster0.6ycjkak.mongodb.net")
USER = os.getenv("USER", "IRGC_NEW")
PASSWORD = os.getenv("PASSWORD", "iran135")
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "tweets")
kaf_config = {
    "bootstrap_servers":"localhost:9092",
        "value_serializer":lambda v: json.dumps(v).encode("utf-8")}

class main:

    def __init__(self):
        self.r = Retriever1(HOST, DB, COLLECTION, USER, PASSWORD,kaf_config)
        self.r.Rstart_pull_100_min()




m=main()






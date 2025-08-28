from persister import Persister
import os
import json


HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "")


kaf_config = {
    'bootstrap_servers' : [f"localhost:9092"],
    'group_id' : "my-consumer",
    'auto_offset_reset' : "earliest",
    'enable_auto_commit' : 'True',
    'value_deserializer' : lambda v: json.loads(v.decode("utf-8"))
}
topics_dal=["enriched_preprocessed_tweets_antisemitic","enriched_preprocessed_tweets_not_antisemitic"]


class main:

    def __init__(self):
        self.p = Persister(HOST, DB, COLLECTION, USER, PASSWORD,kaf_config,topics_dal)

    def pull_from_kafka(self):
        print("--")
        self.p.pull_from_kafka()

m=main()
print("---")
m.pull_from_kafka()

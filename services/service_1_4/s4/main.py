from persister import Persister
import os
import json


HOST = os.getenv("HOST", "localhost")
USER = os.getenv("USER", None)
PASSWORD = os.getenv("PASSWORD",None)
DB = os.getenv("DATABASE", "IranMalDB")
COLLECTION = os.getenv("COLLECTION", "")


kaf_config = {
    'bootstrap_servers' : [f"localhost:9092"],
    'group_id' : "my-consumer",
    'auto_offset_reset' : "earliest",
    'enable_auto_commit' : 'True',
    'value_deserializer' : lambda v: json.loads(v.decode("utf-8"))
}
# topics_client=["enriched_preprocessed_tweets_antisemitic","enriched_preprocessed_tweets_not_antisemitic"]

topics_client=["preprocessed_tweets_antisemitic","preprocessed_tweets_not_antisemitic"]

class main:

    def __init__(self):
        self.p = Persister(HOST, DB, COLLECTION, USER, PASSWORD,kaf_config,topics_client)

    def pull_from_kafka(self):
        print("--")
        self.p.pull_from_kafka()

m=main()
print("---")
m.pull_from_kafka()

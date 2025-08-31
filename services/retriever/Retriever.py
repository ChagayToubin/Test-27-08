from project.classes.fetchers.my_mongodb.MongoBD import DALMongo


class Retriever1:
    def __init__(self,HOST, DB, COLLECTION, USER, PASSWORD,kaf_config):
        self.Mongo=DALMongo(HOST, DB, COLLECTION, USER, PASSWORD,kaf_config)

    def Rstart_pull_100_min(self):
        self.Mongo.Dstart_pull_100_min()
        self.Mongo.kaf.close()






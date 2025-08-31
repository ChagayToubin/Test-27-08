class DataRetrievalManager:

    def __init__(self, fetcher):
        self.fetcher = fetcher


    def read_collection(self, db_name, col_name):
        try:
            self.fetcher.open_connection()
            return list(self.fetcher.client[db_name][col_name].find({}, {"_id": 0}))
        except Exception as e:
            return e
        finally:
            self.fetcher.close_connection()
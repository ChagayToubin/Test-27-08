class FastApiGateway:

    def __init__(self, manager_app, app):
        self.manager_app = manager_app
        self.app = app
        self._all_endpoint()

    def _all_endpoint(self) -> None:

        @self.app.get("/health")
        def health():
            return {"status": "ok"}

        @self.app.get("/get_antisemitic_collection")
        def get_antisemitic_col():
            return self.manager_app.read_collection("IranMalDB", "raw_tweets_antisemitic")

        @self.app.get("/get_not_antisemitic_collection")
        def get_not_antisemitic_col():
            return self.manager_app.read_collection("IranMalDB", "raw_tweets_not_antisemitic")